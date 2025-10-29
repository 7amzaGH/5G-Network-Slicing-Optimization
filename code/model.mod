# model.mod
# Integer Linear Programming model for 5G Network Slicing
# Author: Hamza Ghitri

set Slices;
set Links;
set TimeSlots;

param demand{Slices, Links, TimeSlots};
param capacity{Links};

var x{Slices, Links, TimeSlots} binary;

maximize TotalBandwidth:
    sum {s in Slices, l in Links, t in TimeSlots} demand[s, l, t] * x[s, l, t];

subject to CapacityConstraint {l in Links, t in TimeSlots}:
    sum {s in Slices} demand[s, l, t] * x[s, l, t] <= capacity[l];

subject to FairnessConstraint {s in Slices}:
    sum {l in Links, t in TimeSlots} x[s, l, t] >= 1;
