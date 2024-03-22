function analysis() 
{
    var resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; 
    getAnalysis(resultsDiv);
};
async function getAnalysis(container){
    const response = await fetch(`https://cf0ebb89-401f-4c17-93ed-ce66790377f8-00-21i5m8412bdrv.sisko.repl.co/fundamental?twt=${tweet}`);
    const result = await response.text();
    container.innerHTML =`<div>${result}</div>`;
};