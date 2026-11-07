#!/usr/bin/env python3
"""Mały Szef – podstawowe dźwięki (syntetyzowane, bez licencji obcych). Użycie: python3 soundgen.py out/snd"""
import numpy as np, os, sys, subprocess, wave
OUT = sys.argv[1] if len(sys.argv) > 1 else "out/snd"; os.makedirs(OUT, exist_ok=True)
SR = 44100
def t(d): return np.arange(int(SR * d)) / SR
def env(n, a=.005, r=.2):
    x = np.arange(n) / SR; e = np.minimum(1, x / a) * np.exp(-x / r); return e
def bell(f, d, r=.25, v=1):
    x = t(d); s = np.sin(2*np.pi*f*x) + .4*np.sin(2*np.pi*2*f*x) + .15*np.sin(2*np.pi*3.01*f*x)
    return v * s * env(len(x), .003, r)
def tri(f, d, r=.2, v=1):
    x = t(d); s = 2*np.abs(2*((f*x) % 1) - 1) - 1; return v * s * env(len(x), .005, r)
def at(parts, total):
    out = np.zeros(int(SR * total))
    for start, sig in parts:
        i = int(SR * start); n = min(len(sig), len(out) - i); out[i:i+n] += sig[:n]
    return out
def note(n): return 440 * 2 ** ((n - 69) / 12)   # MIDI
def save(name, sig):
    sig = sig / max(1e-6, np.abs(sig).max()) * .85
    wav = os.path.join(OUT, name + ".wav")
    with wave.open(wav, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((sig * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-codec:a", "libmp3lame", "-b:a", "64k", os.path.join(OUT, name + ".mp3")], check=True)
    os.remove(wav)

# tap – krótkie „pyk”
x = t(.09); f = 500 + 900 * x / .09
save("tap", np.sin(2*np.pi*np.cumsum(f)/SR) * env(len(x), .002, .025))
# found – radosne „ding-ding”
save("found", at([(0, bell(note(84), .5, .18)), (.09, bell(note(88), .6, .25))], .7))
# star – iskierki
save("star", at([(i*.06, bell(note(n), .4, .12, .8)) for i, n in enumerate([84, 88, 91, 96, 100])], .75))
# wrong – łagodne „bu-bum”
save("wrong", at([(0, tri(note(62), .25, .12)), (.16, tri(note(57), .35, .18))], .55))
# success – krótka fanfara
save("success", at([(0, bell(note(72), .3, .15)), (.11, bell(note(76), .3, .15)), (.22, bell(note(79), .3, .15)), (.33, bell(note(84), .7, .35)), (.33, bell(note(76), .7, .35, .5))], 1.1))
# reward – większa fanfara z akordem
seq = [(0, 67), (.13, 72), (.26, 76), (.39, 79), (.6, 84)]
parts = [(s, bell(note(n), .5, .18)) for s, n in seq] + [(.6, bell(note(n), 1.2, .5, .6)) for n in (72, 76, 79)]
save("reward", at(parts, 1.9))
# sticker – „szuuu” + dzwoneczek
x = t(.35); noise = np.random.default_rng(1).standard_normal(len(x))
sw = np.convolve(noise, np.ones(30)/30, "same") * np.sin(np.pi * x / .35) * .6
save("sticker", at([(0, sw), (.3, bell(note(91), .6, .25)), (.38, bell(note(96), .6, .3))], 1.0))
# pop – zmiana zakładki / otwarcie okna
x = t(.12); f = 300 + 300 * x / .12
save("pop", np.sin(2*np.pi*np.cumsum(f)/SR) * env(len(x), .003, .04))
print("OK", sorted(os.listdir(OUT)))
