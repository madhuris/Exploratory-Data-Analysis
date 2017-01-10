Scatterplot.prototype.Scatter_SelectionItem= function(){
  var listSelectedItems = [];
  var listofItemsOnScreen = [];
  d3.selectAll("circle").each(function(d,i) {
    if(d3.select(this).style("visibility")=="visible")
    {
      listofItemsOnScreen.push(i);
    }
  });

  d3.selectAll("circle").each(function(d,i) {
    if(d3.select(this).classed('selected'))
    {
      listSelectedItems.push(i);
    }
  });

//  console.log(listSelectedItems,listofItemsOnScreen);
  var re = new recomEngine("select",listSelectedItems,listofItemsOnScreen);
  re.GetRecom(re);
}
