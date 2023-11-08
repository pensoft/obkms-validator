import os
from lxml import etree as ET
from validator.constants import PensoftXpathConstants, PensoftAttrConstants
from uuid import UUID
import copy

try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request

class Validator():
    
    def __init__(self):
        self._errors = []
        self.__check_nodes = 0
        self._isExecuteValidation = False
    
    def incrementCheckNodes(self):
        self.__check_nodes += 1
    
    def setXml(self, url):
        self.resource = self.load(url)
    
    def tryLoad(self, path):
        try:
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
                'Accept': 'application/xml'
                }
            request = Request(path, headers=headers)
            return urlopen(request, timeout=5)
        except Exception as error:
            self._errors.append(str(error))
            return False
        
    def load(self, path):
        resource = self.tryLoad(path)
        if resource == False:
            return
        
        try:
            return ET.parse(resource)
        except Exception as error:
            self._errors.append(str(error))

    def getResource(self):
        return self.resource
    
    def getRoot(self):
        return self.getResource().getroot()

    def validate(self):
        if self._isExecuteValidation == True:
            return
        
        if self.errors():
            return False
        
        self.isValid(key='ABSTRACT', path=PensoftXpathConstants.ABSTRACT.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        
        self.isValid(key='CONTRIB_GROUP', path=PensoftXpathConstants.CONTRIB_GROUP.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value, isRequired=True)
        self.isValid(key='CONTRIB', path=PensoftXpathConstants.CONTRIB_GROUP.value + '/contrib', obkms_id=PensoftAttrConstants.OBKMS_ID.value, isRequired=True)
        self.isValid(key='BIBLIOGRAPHY', path=PensoftXpathConstants.BIBLIOGRAPHY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value, isRequired=True)
        self.isValid(key='REFERENCE', path=PensoftXpathConstants.REFERENCE.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value, isRequired=True)
        self.isValid(key='BIN', path=PensoftXpathConstants.BIN.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='BOLD_ID', path=PensoftXpathConstants.BOLD_ID.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='CHECKLIST', path=PensoftXpathConstants.CHECKLIST.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='ABBREVIATIONS', path=PensoftXpathConstants.ABBREVIATIONS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        # self.isValid(key='ABBREVIATION', path=PensoftXpathConstants.ABBREVIATION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='ACKNOWLEDGEMENTS', path=PensoftXpathConstants.ACKNOWLEDGEMENTS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='NOTES', path=PensoftXpathConstants.NOTES.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TAXONOMY_SEC', path=PensoftXpathConstants.TAXONOMY_SEC.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='CONTRIBUTIONS', path=PensoftXpathConstants.CONTRIBUTIONS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='DESCRIPTION', path=PensoftXpathConstants.DESCRIPTION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(
            key='FIGURE', 
            path=PensoftXpathConstants.FIGURE.value,
            obkms_id=[PensoftXpathConstants.ARPHA_ID.value, PensoftAttrConstants.OBKMS_ID.value]
        )
        self.isValid(key='GENBANK', path=PensoftXpathConstants.GENBANK.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='INTRODUCTION', path=PensoftXpathConstants.INTRODUCTION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='KEYWORD', path=PensoftXpathConstants.KEYWORD.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='KEYWORDS', path=PensoftXpathConstants.KEYWORD.value+'/kwd', obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='METHODS', path=PensoftXpathConstants.METHODS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TABLE', path=PensoftXpathConstants.TABLE.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TAXONOMIC_KEY', path=PensoftXpathConstants.TAXONOMIC_KEY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='ARTICLE_TITLE', path=PensoftXpathConstants.ARTICLE_TITLE.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(
            key='TNU', 
            path=PensoftXpathConstants.TNU.value, 
            obkms_id=[PensoftXpathConstants.ARPHA_ID.value, PensoftAttrConstants.OBKMS_ID.value]
        )
        self.isValid(
            key='TREATMENT', 
            path=PensoftXpathConstants.TREATMENT.value, 
            obkms_id=[
                "tp:nomenclature/tp:taxon-name/object-id[@content-type='arpha']",
                PensoftAttrConstants.OBKMS_ID.value
            ]
        )
        self.isValid(key='NOMENCLATURE', path=PensoftXpathConstants.NOMENCLATURE.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='NOMENCLATURE_CIT_LIST', path=PensoftXpathConstants.NOMENCLATURE_CIT_LIST.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='NOMENCLATURE_CITATION', path=PensoftXpathConstants.NOMENCLATURE_CITATION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='LIT_CITATION', path=".//back/ref-list/ref", obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TYPE_MATERIAL', path=PensoftXpathConstants.TYPE_MATERIAL.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='USES', path=PensoftXpathConstants.USES.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='ETYMOLOGY', path=PensoftXpathConstants.ETYMOLOGY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TAXONOMY', path=PensoftXpathConstants.TAXONOMY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='ECOLOGY_BIOLOGY', path=PensoftXpathConstants.ECOLOGY_BIOLOGY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='TYPE_LOCALITY', path=PensoftXpathConstants.TYPE_LOCALITY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='DIAGNOSIS', path=PensoftXpathConstants.DIAGNOSIS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='DISTRIBUTION', path=PensoftXpathConstants.DISTRIBUTION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='MORPHOLOGY', path=PensoftXpathConstants.MORPHOLOGY.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='CONSERVATION_STATUS', path=PensoftXpathConstants.CONSERVATION_STATUS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='MOLECULAR_DATA', path=PensoftXpathConstants.MOLECULAR_DATA.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='INSTITUTION', path=PensoftXpathConstants.INSTITUTION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='CONSERVATION', path=PensoftXpathConstants.CONSERVATION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='DATA', path=PensoftXpathConstants.DATA.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='USAGE_RIGHTS', path=PensoftXpathConstants.USAGE_RIGHTS.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='FUNDING', path=PensoftXpathConstants.FUNDING.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(
            key='SUPPLEMENTARY_MATERIAL', 
            path=PensoftXpathConstants.SUPPLEMENTARY_MATERIAL.value, 
            obkms_id=[PensoftXpathConstants.ARPHA_ID.value, PensoftAttrConstants.OBKMS_ID.value]
        )
        self.isValid(key='APPENDIX', path=PensoftXpathConstants.APPENDIX.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        self.isValid(key='GENERAL_SECTION', path=PensoftXpathConstants.GENERAL_SECTION.value, obkms_id=PensoftAttrConstants.OBKMS_ID.value)
        return True
        
    def errors(self):
        return self._errors
    
    def checks(self):
        return self.__check_nodes
    
    def isValid(self, key, path, obkms_id=PensoftAttrConstants.OBKMS_ID.value, isRequired=False):
        root = self.getRoot()
        namespace = root.nsmap
        
        try:
            xpath = ET.XPath(path, namespaces=namespace)
            nodes = xpath(root)
        except Exception:
            nodes = []
        
        if len(nodes) == 0 and isRequired == True:
            self._errors.append("{}: The path in ({}) is missing".format(key, path))
        
        if obkms_id == None:
            return
            
        if not isinstance(obkms_id, list):
            obkms_id = [obkms_id]
            
        for node in nodes:
            obkms_id_ = copy.copy(obkms_id)
            exactPath = self.getResource().getpath(node)
            identifier = None
            self.incrementCheckNodes()
            while len(obkms_id_):
                if identifier != None:
                    break
                _path = obkms_id_.pop(0)

                try:
                    identifier = node.get(_path, None)
                except:
                    pass
                
                if identifier != None:
                    continue
                
                try:
                    _xpath = ET.XPath(_path, namespaces=namespace)
                    _nodes = _xpath(node)
                    for _node in _nodes:
                        identifier = _node.text
                        break
                except:
                    pass

            if identifier == None:
                self._errors.append("{}: The obkms_id in ({}) is missing".format(key, exactPath))
                continue
            try:
                UUID(str(identifier).lower())
            except Exception as error:
                self._errors.append("{}: {} ({})".format(key, str(error), exactPath))
    
# v = V('https://phytokeys.pensoft.net/article/49602/download/xml_obkms_uuids/')
# # v = V('https://phytokeys.pensoft.net/article/49602/download/xml/')
# pprint(v.validate())
# pprint(v.errors())