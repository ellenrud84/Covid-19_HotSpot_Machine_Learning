link= '/Demographics'
d3.json(link).then((Data)=>{
    const data = Data;
    const entries= Object.values(data);
    console.log(entries.length);
    let i;
    for(i=0;i<entries.length;i++){
        let county = entries[i].county_name;
        console.log('county');
        console.log(county);
    
        //  Set the dropdown button with all subject IDs
        d3.select("#selDataset")
            .selectAll("option")
            .data(subjectID)
            .enter()
            .append("option")
            .html(function(d) {
                return d;
            });
    }


});


