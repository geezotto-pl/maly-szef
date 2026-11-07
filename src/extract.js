const fs=require('fs');const s=fs.readFileSync(process.argv[2],'utf8');
function grab(name){const i=s.indexOf('const '+name+'=');let j=i+('const '+name+'=').length;const open=s[j];const close=open==='['?']':'}';let d=0,k=j,str=null;
for(;k<s.length;k++){const c=s[k];if(str){if(c==='\\'){k++;continue}if(c===str)str=null;continue}if(c==='"'||c==="'"||c==='`'){str=c;continue}if(c===open)d++;else if(c===close){d--;if(d===0)break}}
return eval('('+s.slice(j,k+1)+')')}
const ING=grab('ING'),ALLR=grab('ALLR'),PACKDEFS=grab('PACKDEFS'),CATS=grab('CATS'),ALG=grab('ALG');
PACKDEFS.forEach(d=>Object.entries(d.prods||{}).forEach(([k,v])=>{if(!ING[k])ING[k]=v}));
fs.writeFileSync('ms/src.json',JSON.stringify({ING,ALLR,PACKDEFS:PACKDEFS.map(p=>({id:p.id,name:p.name})),CATS,ALG}));
console.log(Object.keys(ING).length,ALLR.length);
const g={};ALLR.forEach(r=>(r.g||[]).forEach(x=>g[x]=(g[x]||0)+1));console.log(g);
console.log(ALLR.filter(r=>r.g.includes('dzieci')).map(r=>r.n+'|'+r.m+'|'+r.t).join('\n'));
console.log(new Set(ALLR.map(r=>r.m)));
