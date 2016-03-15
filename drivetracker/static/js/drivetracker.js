// Magic Django Solution for CSRF Token Validation
var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function formatBytes(bytes,decimals) {
   if(bytes == 0) return '0 Byte';
   var k = 1000; // or 1024 for binary
   var dm = decimals + 1 || 3;
   var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
   var i = Math.floor(Math.log(bytes) / Math.log(k));
   return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

function formatInUse(inUse) {
  if (inUse == 'Yes') return 'Used';
  else if (inUse == 'No') return 'Available';
  return 'Unknown';
}

function drawGraphs () {
    (function(d3) {
      d3.select('body').selectAll('svg').remove();
      // 'use strict';
      var width = 200,
        height = 200,
        radius = Math.min(width, height) / 2,
        donutWidth = 50,
        legendRectSize = 18,
        legendSpacing = 4,
        color = d3.scale.category20();

      // Common graphing variables
      var arc = d3.svg.arc()
        .innerRadius(radius - donutWidth)
        .outerRadius(radius);

      var pie = d3.layout.pie()
        .value(function(d) { return d.count; })
        .sort(null);

      // Manufacturer's Graph
      var manufacturersSvg = d3.select('#manufacturer-graph')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

      // Capacity Graph
      var capacitySvg = d3.select('#capacity-graph')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

      // Status Graph
      var statusSvg = d3.select('#status-graph')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

      // Interface Graph
      var interfaceSvg = d3.select('#interface-graph')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");

      d3.json(driveAPIUrl + '?representation=original', function(error, dataset) {
        var manufacturers = {};
        var capacities = {};
        var statuses = {};
        var interfaces = {};

        dataset.forEach(function(drive) {
          var manufacturer = drive.manufacturer;
          var inUse = formatInUse(drive.in_use);
          var status = drive.status;
          var interface = drive.interface;


          manufacturers[manufacturer] = manufacturers[manufacturer] ? manufacturers[manufacturer] + 1 : 1;
          capacities[inUse] = capacities[inUse] ? capacities[inUse] + drive.capacity : drive.capacity;
          statuses[status] = statuses[status] ? statuses[status] + 1 : 1;
          interfaces[interface] = interfaces[interface] ? interfaces[interface] + 1 : 1;
        });

        manufacturers = $.map(manufacturers, function(value, index) {
          return [{"label": index, "count": value}];
        });
        capacities = $.map(capacities, function(value, index) {
          return [{"label": index, "count": value}]
        })
        statuses = $.map(statuses, function(value, index) {
          return [{"label": index, "count": value}]
        })
        interfaces = $.map(interfaces, function(value, index) {
          return [{"label": index, "count": value}]
        })

        // Draw the graph for the Manufacturer's Graph
        var manufacturersPath = manufacturersSvg.selectAll('path')
          .data(pie(manufacturers))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) {
            return color(d.data.label);
          });

        // Add tooltips to the Manufacturer's Graph
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

        // Draw the graph for the Capacity Graph
        var capacityPath = capacitySvg.selectAll('path')
          .data(pie(capacities))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) {
            return color(d.data.label);
          });

        // Add tooltips to the Capacity Graph
        capacityPath.each(function(d,i) {
          var total = d3.sum(capacities.map(function(d) {
            return d.count;
          }));
          var percent = Math.round(1000 * d.data.count / total) / 10;
          var popover = $(capacityPath[0][i]).popover({
            'container': 'body',
            'title': d.data.label,
            'content': percent + '% of ' + formatBytes(total),
            'trigger': 'hover focus'
          });
        })

        // Draw the graph for the Status Graph
        var statusPath = statusSvg.selectAll('path')
          .data(pie(statuses))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) {
            return color(d.data.label);
          });

        // Add tooltips to the Capacity Graph
        statusPath.each(function(d,i) {
          var total = d3.sum(statuses.map(function(d) {
            return d.count;
          }));
          var percent = Math.round(1000 * d.data.count / total) / 10;
          var popover = $(statusPath[0][i]).popover({
            'container': 'body',
            'title': d.data.label,
            'content': percent + '% of ' + total + ' drives',
            'trigger': 'hover focus'
          });
        })

        // Draw the graph for the Interface Graph
        var interfacePath = interfaceSvg.selectAll('path')
          .data(pie(interfaces))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d, i) {
            return color(d.data.label);
          });

        // Add tooltips to the Capacity Graph
        interfacePath.each(function(d,i) {
          var total = d3.sum(interfaces.map(function(d) {
            return d.count;
          }));
          var percent = Math.round(1000 * d.data.count / total) / 10;
          var popover = $(interfacePath[0][i]).popover({
            'container': 'body',
            'title': d.data.label,
            'content': percent + '% of ' + total + ' drives',
            'trigger': 'hover focus'
          });
        })

      });
    })(window.d3);
  }

var lastDriveId = null;

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
    lastDriveId = table.row(this).data().id;
    var form = $('#hard-drive-form');
    $.ajax({
      url: driveFormUrl + lastDriveId + '/',
      type: "GET",
      success: function(data) {
        $(form).replaceWith(data['form_html']);
        $('#add-new-drive-modal-label').text('Edit Drive ' + lastDriveId);
        $('#add-new-drive-modal').modal('show');
      }
    });
  });

  $('#save-hard-drive-button').on('click', function() {
    var form = $('#hard-drive-form');
    var submissionUrl = driveFormUrl;
    if (lastDriveId != null) {
       submissionUrl = driveFormUrl + lastDriveId + '/';
       lastDriveId = null;
    }
    $.ajax({
      url: submissionUrl,
      type: "POST",
      data: $(form).serialize(),
      success: function(data) {
        if (!(data['success'])) {
          $(form).replaceWith(data['form_html']);
        }
        else {
          $('#add-new-drive-modal').modal('hide');
        }
      },
      error: function () {
        $(form).find('.error-message').show();
      }
    });
  });

  $('#add-new-drive-modal').on('hidden.bs.modal', function() {
    $('#drive-table').DataTable().ajax.reload(null, false);
    drawGraphs();
    $('#add-new-drive-modal-label').text('Add New Drive');
    var form = $('#hard-drive-form');
    $.ajax({
      url: driveFormUrl,
      type: "GET",
      success: function(data) {
        $(form).replaceWith(data['form_html']);
      }
    });
  });

  $('#add-new-drive-modal').on('show.bs.modal', function() {
    $('.dateinput').datetimepicker({'format': 'MM/DD/YYYY'});
  });

  drawGraphs();

  // Allow autocomplete to work inside the Bootstrap Modal
  $.fn.modal.Constructor.prototype.enforceFocus = function() {};
});
