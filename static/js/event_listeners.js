// POPULATE DROPDOWN MENU WITH ALL COUNTIES 
const link= '/Demographics';
// casesLink='/48201';
// mobLink= '48201_Full'

d3.json(link).then((Data)=>{
    const data = Data;
    const entries= Object.values(data);
    // console.log('entries')
    // console.log(entries)
    let i;
    countyList=[]
    for(i=0; i<entries.length; i++){
        county_i =entries[i]
        // console.log(county_i);
        name= county_i['county_name']
        // console.log(name)
        countyList.push(name)
    };
    // console.log(countyList)
       
    //  Set the dropdown button with all subject IDs
    d3.select("#selDataset")
        .selectAll("option")
        .data(countyList)
        .enter()
        .append("option")
        .html(function(d) {
            return d;
        })   
});

// initialize with Harris county data
function init(){
    // let casesLink='/Harris';
    let mobLink='/Harris_Full'
    buildPlots("Harris", mobLink);
}

init();

// POPULATE INTERACTIVE CHARTS BASED ON CHOSEN COUNTY
//handle changes in the dropdown selector
function optionChanged (){
    const dropDownMenu= d3.select('#selDataset');
    const county = dropDownMenu.property('value');
    // console.log(county);
    let casesLink='/'+county;
    let mobLink='/'+county+'_Full'
  
    buildPlots(county, mobLink);

};


function buildPlots(county, mobLink){

    // populate the header with the correct county
    let cty= county
    console.log(`cty: ${cty}`)
    let textHeader= `${cty} County Historical Data and Projections`;
    console.log(`textHeader: ${textHeader}`)
    d3.select("h1.myClass").append("span").text=textHeader

    // create charts
    d3.json(mobLink).then((Data)=>{
        const data = Data;
        const entries= Object.values(data);
        let filterData=entries.filter(i=>i.county_name===county)
        // console.log('Data filtered to county:')
        // console.log(filterData)
        // console.log('entries')
        // console.log(entries)

        let i;
        let casesList=[];
        let deathsList=[];
        let datesList=[];
        let grocList=[];
        let parksList=[];
        let resList=[];
        let retailList=[];
        let transitList=[];
        let workList=[];

        for(i=0; i<filterData.length; i++){
            time_i =filterData[i]
            // console.log(time_i);

            date=new Date(time_i['date']);
            cases=time_i['cases'];
            deaths=time_i['deaths'];
            mob_groc=time_i['grocery_and_pharmacy_percent_change_from_baseline'];
            mob_parks=time_i["parks_percent_change_from_baseline"];
            mob_res=time_i['residential_percent_change_from_baseline']
            mob_retail=time_i['retail_and_recreation_percent_change_from_baseline']
            mob_transit=time_i['transit_stations_percent_change_from_baseline']
            mob_work=time_i['workplaces_percent_change_from_baseline']
            
            // console.log(`date:${date}`);
            // console.log(`cases:${cases}`);
            // console.log(`deaths:${deaths}`);
            
            datesList.push(date);
            casesList.push(cases);
            deathsList.push(deaths);
            grocList.push(mob_groc);
            parksList.push(mob_parks);
            resList.push(mob_res);
            retailList.push(mob_retail);
            transitList.push(mob_transit);
            workList.push(mob_work);
        };
        // console.log(`datesList:${datesList}`);
        // console.log(`casesList:${casesList}`);
        // console.log(`deathsList:${deathsList}`);
           
        // create plots:

        const trace1={
            x:datesList,
            y:casesList,
            type:'line'
        };

        const trace2={
            x:datesList,
            y:deathsList,
            type:'line',
            line:{color:'red'}
        };

        const trace3={
            x:datesList,
            y:grocList,
            type:'line',
            line:{color:'red'}
        };

        const trace4={
            x:datesList,
            y:parksList,
            type:'line',
            line: {color: "orange"}
        };

        const trace5={
            x:datesList,
            y:resList,
            type:'line',
            line: {color:"green"}
        };

        const trace6={
            x:datesList,
            y:retailList,
            type:'line',
            line: {color:'blue'}
        };

        const trace7={
            x:datesList,
            y:transitList,
            type:'line',
            line:{color:'purple'}
        };

        const trace8={
            x:datesList,
            y:workList,
            type:'line',
            line: {color:'black'}
        };

        const layout1={
            yaxis:{title:'Cases', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout2={
            yaxis:{title:'Deaths', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };

        const layout3={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout4={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout5={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout6={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout7={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };
        const layout8={
            yaxis:{title:'% Change Mobility', automargin:true},
            xaxis:{title:'Date'},
            autosize: true
        };

        Plotly.newPlot('casesPlot', [trace1], layout1);
        Plotly.newPlot('deathsPlot', [trace2], layout2);
        Plotly.newPlot('mobGroc', [trace3], layout3);
        Plotly.newPlot('mobParks', [trace4], layout4);
        Plotly.newPlot('mobRes', [trace5], layout5);
        Plotly.newPlot('mobRetail', [trace6], layout6);
        Plotly.newPlot('mobTransit', [trace7], layout7);
        Plotly.newPlot('mobWork', [trace8], layout8);
       
        // TODO: EDIT CODE BELOW FOR RESPONSIVE FIGURES FOR MOBILE
        // make plotly plots responsive to resizing page
        // ref: https://gist.github.com/aerispaha/63bb83208e6728188a4ee701d2b25ad5
        // (function resize(){
        //     var d3 = Plotly.d3;
        //     var WIDTH_IN_PERCENT_OF_PARENT = 90,
        //         HEIGHT_IN_PERCENT_OF_PARENT = 80;
            
        //     var gd3 = d3.selectAll(".responsive-plot")
        //         .style({
        //           width: WIDTH_IN_PERCENT_OF_PARENT + '%',
        //           'margin-left': (100 - WIDTH_IN_PERCENT_OF_PARENT) / 2 + '%',
                  
        //           height: HEIGHT_IN_PERCENT_OF_PARENT + 'vh',
        //           'margin-top': (100 - HEIGHT_IN_PERCENT_OF_PARENT) / 2 + 'vh',

        //           'border-radius': '20px'
        //         });
          
        //     var nodes_to_resize = gd3[0]; //not sure why but the goods are within a nested array
        //     window.onresize = function() {
        //       for (var i = 0; i < nodes_to_resize.length; i++) {
        //         Plotly.Plots.resize(nodes_to_resize[i]);
        //       }
        //     };
            
        //   })();
    });

    // pull demogs for that county:
    d3.json(link).then((Data)=>{
        const data = Data;
        const entries= Object.values(data);
        const filterDemogs=entries.filter(i=>i.county_name===county);
        // console.log('demogsfiltered to county:');
        // console.log(filterDemogs[0]);
        const demogs=filterDemogs[0];

        // // list of all demogs
        // // POPULATION
        // "County_Population" 
        // "Percent_Rural": 67.06,
        // "Percent_Urban": 32.94, 
        const popDensity=demogs.Population_Density_per_Sq_Mile;
        document.getElementById("density").innerHTML=`<h3> ${Math.round(popDensity)}</h3>`;
        // "RUCC_2013": 7, 
        // "RUCC_Description": "Nonmetro - Urban population of 2,500 to 19,999, not adjacent to a metro area 
        
        // INCOME
        // "Avg_Annual_Pay"
        // "Median_Household_Income" 
        const income=demogs.Per_Capita_Income;

        // RACE
        const black=demogs.Percent_African_American_Alone;
        const native=demogs['Percent_American_Indian_&_Alaska_Native_Alone'];
        const asian= demogs.Percent_Asian_Alone;
        const hispanic=demogs.Percent_Hispanic;
        const multiracial =demogs.Percent_Multi_Racial;
        const pacific_islander= demogs.Percent_Native_Hawaiian_and_Other_Pacific_Islander_Alone;
        const white= demogs.Percent_White_Alone;

        raceNumbers=[black, native, asian, hispanic, multiracial, pacific_islander, white];
        
        const raceData=[{
            values: raceNumbers,
            labels:['African Amer.', 'Native Amer.', 'Asian','Hispanic', 'Multiracial', 'Pac. Islander', 'Caucasian'],
            type: 'pie',
            hoverinfo: 'label+percent+name',
            textinfo: "label+percent",
            sort:false
        }];

        const raceLayout={
            height:300,
            width: 400,
            margin:{"t":20,"b":0, "l":100, "r":100},
            showlegend:false
        };

        Plotly.newPlot('race', raceData, raceLayout)

        

        // AGE GROUP PERCENTAGES
        const medAge=demogs.Median_Age;
        // document.getElementById("age").innerHTML=`<h3> ${Math.round(medAge)}</h3>`;
        const Age_17_and_Under=demogs.Percent_Age_17_and_Under;
        console.log(`<17, ${Age_17_and_Under}`)

        const Age_65_and_Older=demogs.Percent_Age_65_and_Older;
        console.log(`>65, ${Age_65_and_Older}`)

        const Age_85_and_Older=demogs.Percent_Age_85_and_Older;
        console.log(`>85, ${Age_85_and_Older}`)

        const Age_18_to_64=100-Age_17_and_Under-Age_65_and_Older;
        console.log(`18-64, ${Age_18_to_64}`)

        const Age_65_to_84=Age_65_and_Older-Age_85_and_Older;
        console.log(`65-84, ${Age_65_to_84}`)

        // create age breakdown chart:
        ageNumbers=[Age_17_and_Under, Age_18_to_64, Age_65_to_84,Age_85_and_Older ]

        const ageData=[{
            values: ageNumbers,
            labels:['<17', '18-64', '65-84','>85'],
            type: 'pie',
            hoverinfo: 'label+percent+name',
            textinfo: "label+percent",
            textposition: "inside",
        }];

        const ageLayout={
            height:200,
            width:200,
            margin:{"t":0,"b":0, "l":0, "r":0},
            showlegend:false
        };

        Plotly.newPlot('age', ageData, ageLayout)
        

        // EDUCATION
        const college= demogs.Percent_Bachelors_Degree_or_Higher;
        const HS_and_higher= demogs.Percent_HS_Graduate_or_Higher;
        const no_HS=100-HS_and_higher;
        const HS= HS_and_higher-college

        // create education plot
        edNumbers=[no_HS, HS, college]

        const edData=[{
            values: edNumbers,
            labels:['no HS', 'HS Grad', 'College Grad +'],
            type: 'pie',
            hoverinfo: 'label+percent+name',
            textinfo: "label+percent",
            textposition: "inside",
        }];

        const edLayout={
            height:200,
            width:200,
            margin:{"t":0,"b":0, "l":0, "r":0},
            showlegend:false
        };

        Plotly.newPlot('education', edData, edLayout)

        // INSURANCE
        // "Percent_Insured": 80.1
        const uninsured=demogs.Percent_Uninsured;
        document.getElementById("insurance").innerHTML=`<h3> ${Math.round(uninsured)}</h3>`;
        
        // POVERTY
        const poverty=demogs.Percent_Population_in_Poverty;
        document.getElementById("poverty").innerHTML=`<h3> ${Math.round(poverty)}</h3>`;
        const youth_poverty=demogs.Percent_Population_under_18_in_Poverty;

        // // EMPLOYMENT
        const unemployment=demogs.Percent_Unemployed;

        // // LOCATION:
        const fips=demogs.fips_code;
    });


};