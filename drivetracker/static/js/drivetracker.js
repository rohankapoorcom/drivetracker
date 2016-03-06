function formatBytes(bytes,decimals) {
   if(bytes == 0) return '0 Byte';
   var k = 1000; // or 1024 for binary
   var dm = decimals + 1 || 3;
   var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
   var i = Math.floor(Math.log(bytes) / Math.log(k));
   return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

$(document).ready(function() {
  $('#drive-table').DataTable( {
    "ajax": {
      url: driveAPIUrl,
      dataSrc: ''
    },
    "columns": [
      {"data": "id"},
      {"data": "host"},
      {"data": "serial"},
      {"data": "media_type"},
      {"data": "in_use"},
      {"data": "status"},
      {"data": "manufacturer"},
      {"data": "model"},
      {"data": "capacity"},
      {"data": "interface"},
      {"data": "rpm"}
    ]
  });

  $('#drive-table tbody').on('click', 'tr', function() {
    var table = $('#drive-table').DataTable();
    var data = table.row(this).data().id;
    console.log(data);
  });
  (function(d3) {
    'use strict';
    var width = 200,
      height = 200,
      radius = Math.min(width, height) / 2,
      donutWidth = 50,
      legendRectSize = 18,
      legendSpacing = 4,
      color = d3.scale.category20();

    /* Common graphing variables */
    var arc = d3.svg.arc()
      .innerRadius(radius - donutWidth)
      .outerRadius(radius);

    var pie = d3.layout.pie()
      .value(function(d) { return d.count; })
      .sort(null);

    /* Manufacturer's Graph */
    var manufacturersSvg = d3.select('#manufacturer-graph')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

    /* Capacity Graph */
    var capacitySvg = d3.select('#capacity-graph')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

    d3.json(driveAPIUrl + '?representation=original', function(error, dataset) {
      var manufacturers = {};
      var capacities = {};

      dataset.forEach(function(drive) {
        var manufacturer = drive.manufacturer;
        var in_use = drive.in_use == null || drive.in_use == false ? 'Available' : 'In Use';

        manufacturers[manufacturer] = manufacturers[manufacturer] ? manufacturers[manufacturer] + 1 : 1;
        capacities[in_use] = capacities[in_use] ? capacities[in_use] + drive.capacity : drive.capacity;
      });

      manufacturers = $.map(manufacturers, function(value, index) {
        return [{"label": index, "count": value}];
      });
      capacities = $.map(capacities, function(value, index) {
        return [{"label": index, "count": value}]
      })

      /* Draw the graph for the Manufacturer's Graph */
      var manufacturersPath = manufacturersSvg.selectAll('path')
        .data(pie(manufacturers))
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function(d, i) {
          return color(d.data.label);
        });

      /* Add tooltips to the Manufacturer's Graph */
      manufacturersPath.each(function(d,i) {
        var total = d3.sum(manufacturers.map(function(d) {
          return d.count;
        }));
        var percent = Math.round(1000 * d.data.count / total) / 10;
        var popover = $(manufacturersPath[0][i]).popover({
          'container': 'body',
          'title': d.data.label,
          'content': percent + '% of ' + total + ' drives',
          'trigger': 'hover focus'
        });
      })

      /* Draw the graph for the Capacity Graph */
      var capacity_path = capacitySvg.selectAll('path')
        .data(pie(capacities))
        .enter()
        .append('path')
        .attr('d', arc)
        .attr('fill', function(d, i) {
          return color(d.data.label);
        });

      /* Add tooltips to the Capacity Graph */
      capacity_path.each(function(d,i) {
        var total = d3.sum(capacities.map(function(d) {
          return d.count;
        }));
        var percent = Math.round(1000 * d.data.count / total) / 10;
        var popover = $(capacity_path[0][i]).popover({
          'container': 'body',
          'title': d.data.label,
          'content': percent + '% of ' + formatBytes(total),
          'trigger': 'hover focus'
        });
      })

    });
  })(window.d3);
});
