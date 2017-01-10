
originalColor ="#267bfb";
originalRadius = 5;

margin = {top: 10, right: 150, bottom: 4, left: 20},
width = (82/100)* window.innerWidth- margin.left - margin.right,
height = (90/100)* window.innerHeight- margin.top - margin.bottom;

console.log("I am here");

function startVis (dataset) {
  svg = d3.select("body").select("#VisContainer").append("svg")
              .attr("id","Vis")
              .attr("width", width + margin.left + margin.right)
              .attr("height", height + margin.top + margin.bottom)
              .append("g")
              .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  gdots =  svg.selectAll("g.dot")
              .data(dataset)
              .enter().append('g')
              .attr("class", "dot")
              .attr("id", function(d,i){return "g_id_"+d.id;})
              .attr("transform", function(d,i){
                    d.x = Math.floor((Math.random() * width ));
                    d.y = Math.floor((Math.random() * height));
                    return "translate("+d.x+","+d.y+")"
              });
                  //.call(dragCircle);

  gdots.append("circle")
       .attr("class", "circle")
       .attr("fill", function(d,i){
         d.color = originalColor;
         return d.color;
       })
       .style("opacity", 0.5)
       .attr("id", function(d,i){return "id_"+d.id;})
       .attr("r", function(d){
              d.r = originalRadius;
              return d.r;
        })
        .on('mouseenter', function(d,i) {
              ShowDetail(i);
        });
}

function updateVis2(listedItems) {
  d3.selectAll("circle").style("visibility",function(d){
      if(d[listedItems]!="0"){
        return "visible";
      }
      else {
        return "hidden";
      }
  })
}

function updateVis(listedItems) {
//  console.log(listedItems)
  d3.selectAll("circle").style("visibility",function(d){
    var meetsCondition = "visible";
    for(var listedItem of listedItems){
      if(d[listedItem]=="0"){
        meetsCondition = "invisible";
        break;
      }
    }
    if(meetsCondition=="visible"){
      return "visible";
    }else {
      return "hidden";
    }
  })
}
