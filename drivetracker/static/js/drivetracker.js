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

// Common graphing variables
var width = 200,
  height = 200,
  radius = Math.min(width, height) / 2,
  donutWidth = 50,
  legendRectSize = 18,
  legendSpacing = 4,
  color = d3.scale.category20c();

var arc = d3.svg.arc()
  .innerRadius(radius - donutWidth)
  .outerRadius(radius);

var pie = d3.layout.pie()
  .value(function(d) { return d.count; })
  .sort(null);

function drawSvg(selector) {
  return d3.select(selector)
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .append('g')
    .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");
}

function drawPath(svg, dataArray) {
  return svg.selectAll('path')
    .data(pie(dataArray))
    .enter().append('path')
      .attr('fill', function(d, i) { return color(d.data.label); })
      .attr('d', arc)
      .each(function(d) {this._current = d; });
}

// Maps the object to an array of objects containing labels and counts
function mapper(value, index) {
  return [{"label": index, "count": value}];
}

function changeDataInPath(svg, path, dataArray) {
  // Calculate changes in existing paths and transition to them
  svg.selectAll("path").data(pie(dataArray)).transition().duration(1000).attrTween("d", arcTween).each("end", drawTooltips);

  // Add new paths
  svg.selectAll("path")
    .data(pie(dataArray))
  .enter().append('path')
    .attr('fill', function(d, i) { return color(d.data.label); })
    .attr('d', arc)
    .each(function(d) {this._current = d; });

  // Remove unneeded paths
  svg.selectAll("path")
    .data(pie(dataArray)).exit().remove();
}

// Store the displayed angles in _current.
// Then, interpolate from _current to the new angles.
// During the transition, _current is updated in-place by d3.interpolate.
function arcTween(a) {
  var i = d3.interpolate(this._current, a);
  this._current = i(1);
  return function(t) {
    return arc(i(t));
  };
}

function drawTooltips() {
  console.log(true);
}

var manufacturersSvg = drawSvg('#manufacturer-graph'),
  capacitySvg = drawSvg('#capacity-graph'),
  statusSvg = drawSvg('#status-graph'),
  interfaceSvg = drawSvg('#interface-graph');

var alreadyDrewPaths = false;
  manufacturersPath = null,
  capacityPath = null,
  statusPath = null,
  interfacePath = null;

var popovers = [];

function drawGraphs() {
  d3.json(driveAPIUrl + '?representation=original', function(error, dataset) {
    var manufacturers = {},
      capacities = {},
      statuses = {},
      interfaces = {};

    dataset.forEach(function(drive) {
      var manufacturer = drive.manufacturer,
        inUse = formatInUse(drive.in_use),
        status = drive.status,
        interface = drive.interface;

      manufacturers[manufacturer] = manufacturers[manufacturer] ? manufacturers[manufacturer] + 1 : 1;
      capacities[inUse] = capacities[inUse] ? capacities[inUse] + drive.capacity : drive.capacity;
      statuses[status] = statuses[status] ? statuses[status] + 1 : 1;
      interfaces[interface] = interfaces[interface] ? interfaces[interface] + 1 : 1;
    });

    manufacturers = $.map(manufacturers, mapper);
    capacities = $.map(capacities, mapper);
    statuses = $.map(statuses, mapper);
    interfaces = $.map(interfaces, mapper);

    // Draw the graphs
    if (!alreadyDrewPaths) {
      manufacturersPath = drawPath(manufacturersSvg, manufacturers);
      capacityPath = drawPath(capacitySvg, capacities);
      statusPath = drawPath(statusSvg, statuses);
      interfacePath = drawPath(interfaceSvg, interfaces);
      alreadyDrewPaths = true;
    }

    else {
      while(popovers.length) {
        $(popovers.pop()).popover('destroy');
      }

      changeDataInPath(manufacturersSvg, manufacturersPath, manufacturers);
      changeDataInPath(capacitySvg, capacityPath, capacities);
      changeDataInPath(statusSvg, statusPath, statuses);
      changeDataInPath(interfaceSvg, interfacePath, interfaces);
    }

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
      popovers.push(popover);
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
      popovers.push(popover);
    });

    // Add tooltips to the Status Graph
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
      popovers.push(popover);
    });

    // Add tooltips to the Interface Graph
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
      popovers.push(popover);
    });
  });
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
        $('#delete-hard-drive-button').removeClass('hidden');
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

  $('#delete-hard-drive-button').on('click', function() {
    $('#delete-warning').removeClass('hidden');
    $('#delete-hard-drive-button').prop('disabled', true);
  });

  $('#confirm-delete-hard-drive-button').on('click', function() {
    $.ajax({
      url: driveDetailUrl + lastDriveId + '/',
      type: "DELETE",
      success: function(data) {
        $('#add-new-drive-modal').modal('hide');
      }
    });
  });

  $('#cancel-delete-hard-drive-button').on('click', function() {
    $('#delete-warning').addClass('hidden');
    $('#delete-hard-drive-button').prop('disabled', false);
  })

  $('#add-new-drive-modal').on('hidden.bs.modal', function() {
    $('#drive-table').DataTable().ajax.reload(null, false);
    drawGraphs();
    $('#add-new-drive-modal-label').text('Add New Drive');
    $('#delete-hard-drive-button').addClass('hidden');
    $('#delete-warning').addClass('hidden');
    $('#delete-hard-drive-button').prop('disabled', false);
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
