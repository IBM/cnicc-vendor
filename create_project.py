#!/usr/local/bin/python3
import jinja2
import os
import shutil
import sys

project_name = sys.argv[1]

os.mkdir(project_name)
shutil.copytree("./templates/fixtures", "%s/fixtures" % project_name)
shutil.copytree("./templates/test", "%s/test" % project_name)

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

os.mkdir("%s/descriptors" % project_name)

template = templateEnv.get_template("assembly.yml.j2")
output = template.render(name=project_name)
with open("%s/descriptors/%s-assembly.yml" %(project_name, project_name), "w") as descriptor:
    descriptor.write(output)

os.makedirs("%s/resources/%s/1.0/Service-Template" % (project_name, project_name))

with open("%s/resources/%s/1.0/Service-Template/%s-assembly.yml" % (project_name, project_name, project_name), "w") as resource:
    resource.write(output)

resource_template = templateEnv.get_template("resource.yml.j2")
output = resource_template.render(name=project_name)

os.makedirs("%s/resources/%s/1.0/descriptor" % (project_name, project_name))
with open("%s/resources/%s/1.0/descriptor/%s.yml" % (project_name, project_name, project_name), "w") as resource:
    resource.write(output)

os.makedirs("%s/resources/%s/1.0/lifecycle" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Configure.yml" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Install.yml" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Integrity.yml" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Start.yml" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Stop.yml" % (project_name, project_name))
shutil.copyfile("./templates/lifecycle.yml", "%s/resources/%s/1.0/lifecycle/Uninstall.yml" % (project_name, project_name))

feature_template = templateEnv.get_template("resource.feature.j2")
output = feature_template.render(name=project_name)

with open("%s/test/resource.feature" % project_name, "w") as feature:
    feature.write(output)

