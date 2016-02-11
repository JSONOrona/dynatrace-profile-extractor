# Modules
import xml.etree.ElementTree as ET
import re

# Global Variables
FILE = 'application.profile.xml'
# Load and parse the document
tree = ET.ElementTree(file=FILE)

# Fetch the root element and move down an element
root = tree.getroot()[0]

# Test functions
def varTest(var):
    if var:
        return True
    else:
        return False

def getRules():
    # Gets incident rule data
    for elem in root.getiterator(tag='incidentrule'):
        for sub_elem in elem.getiterator(tag='condition'):
            incident_rule_id = elem.attrib['id']
            reference_measure_id = sub_elem.attrib['refmeasure']
            evaluation = sub_elem.attrib['logicaloperator']
            threshold = getMeasures(reference_measure_id)
            print "%s|\t%s|\t%s|\t%s|\t" % (incident_rule_id,reference_measure_id,evaluation,threshold)

def getMeasures(id):
    for elem in root.getiterator('measure'):
        for sub_elem in elem.getiterator('thresholds'):
            measure_id = elem.attrib['id']
            threshold = sub_elem.attrib
            if re.search(id, measure_id):
               if varTest(threshold):
                   return str(threshold).strip("{}")

if __name__ == '__main__':
    print "Incident Rule\t|\tMeasure\t|\tEvaluation\t|\tThreshold\t|"
    getRules()
