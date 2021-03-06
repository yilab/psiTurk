// Generated by CoffeeScript 1.6.3
var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(["backbone", "models/WorkerModel"], function(Backbone, WorkerModel) {
  var Workers, _ref;
  return Workers = (function(_super) {
    __extends(Workers, _super);

    function Workers() {
      this.fetch = __bind(this.fetch, this);
      this.count = __bind(this.count, this);
      _ref = Workers.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    Workers.prototype.model = WorkerModel;

    Workers.prototype.url = "/get_workers";

    Workers.prototype.parse = function(resp) {
      return this.allModels = resp.workers;
    };

    Workers.prototype.initialize = function() {
      return this.reset(this.allModels);
    };

    Workers.prototype.count = function() {
      return this.filteredModels.length;
    };

    Workers.prototype.fetch = function(options) {
      var fetchPromise,
        _this = this;
      fetchPromise = $.ajax({
        url: this.url,
        type: "GET",
        success: function(data) {
          return _this.allModels = data.workers;
        }
      });
      return fetchPromise.done(function() {
        var offset, page, size;
        _this.filteredModels = _.chain(_this.allModels).filter(function(m) {
          return (options.data.type == null) || options.data.type === "" || m.type === options.data.type;
        }).filter(function(m) {
          return (options.data.name == null) || m.name.toLowerCase().indexOf(options.data.name.toLowerCase()) >= 0;
        }).sortBy(options.data.sort_col).tap(function(o) {
          return options.data.sort_dir === "desc" && o.reverse();
        }).value();
        page = options.data.page;
        size = 25;
        offset = (page - 1) * size;
        return _this.reset(_.first(_.rest(_this.filteredModels, offset), size));
      });
    };

    return Workers;

  })(Backbone.Collection);
});
