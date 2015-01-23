(function() {
indexViewModel = function(){
    var self = this;
    self.Tab = function(id, name, text, selected){
        var tab = this;
        tab.id = ko.observable(id);
        tab.name = ko.observable(name);
        return tab;
    };
    self.selectedTab = ko.observable(1);
    self.tabs = new Array();
    self.tabs.push(new self.Tab(1, 'Deity'));
    self.tabs.push(new self.Tab(2, 'Power Boost'));
    self.tabs.push(new self.Tab(3, 'Training'));
    self.tabs.push(new self.Tab(4, 'Cooperative'));
    self.tabs.push(new self.Tab(5, 'Power'));
};
}).call(this);