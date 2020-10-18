// // Code for creating county drop-down
// d3.json("/Demographics", function(data) {
//   // form array of unique counties
//   var counties = data.map(counties => counties.county_name).sort()
//   var uniqueCounties = counties.filter((x, ind, arr) => arr.indexOf(x) === ind)
  
//   // Append counties to dropdown
//   uniqueCounties.forEach(function(county) {
//     var countyDropdown = d3.select("#selCounty").append("option");
//     countyDropdown.text(county);
//   });
// });
  
  
  
  