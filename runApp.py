with open('in.txt') as f:
    lines = f.readlines()

inputs = {}

for line in lines:
    kv = line.rstrip().split("=")
    key = kv[0]
    value = kv[1]
    inputs[key] = value

outputs = "outputs="+str(inputs)
outputTemplate = "\noutputTemplate=<p>Inputs were:</p><p>{{outputs}}</p>"

target = open("out.txt", 'w')
target.write(outputs+outputTemplate)
target.close