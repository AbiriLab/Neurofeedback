import csv 
import pygds as g
d = g.GDS()
minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0]
d.SamplingRate, d.NumberOfScans = minf_s
for ch in d.Channels:
    ch.Acquire = True
d.SetConfiguration()
scope=g.Scope(1/d.SamplingRate)
data = d.GetData(d.SamplingRate,scope)

with open('egg_data.csv', 'w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(data)
