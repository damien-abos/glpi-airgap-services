# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Schema definition, based on Cerberus grammar. Check the Cerberus project
# (https://github.com/pyeve/cerberus) for details.
registrationInfos = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'is_valid': {
            'type': 'boolean',
        },
        'owner': {
            'type': 'dict',
            'schema': {
                'name': {'type': 'string'},
            },
        },
        'subscription': {
            'type': 'dict',
            'schema': {
                'offer_reference': {'type': 'string'},
                'title': {'type': 'string'},
                'is_running': {'type': 'boolean'},
                'begin_date': {'type': 'datetime', 'nullable': True},
                'end_date': {'type': 'datetime', 'nullable': True},
                'features': {'type': 'list'},
            },
        },
    },
}

offers = {
    'schema': {
        'offer_reference': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'title': {
            'type': 'string',
        },
        'features': {
            'type': 'list'
        },
    }
}

plugins = {
    'schema': {
        'id': {
            'type': 'integer',
            'required': True,
            'unique': True,      
        },
        'key': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'name': {
            'type': 'string',
            'required': True,
        },
        'logo_url': {
            'type': 'string',
        },        
        'xml_url': {
            'type': 'string',
        },        
        'homepage_url': {
            'type': 'string',
        },        
        'download_url': {
            'type': 'string',
        },        
        'issues_url': {
            'type': 'string',
        },        
        'readme_url': {
            'type': 'string',
        },        
        'changelog_url': {
            'type': 'string',
        },        
        'license': {
            'type': 'string',
        },        
        'date_added': {
            'type': 'datetime',
        },        
        'date_updated': {
            'type': 'datetime',
        },        
        'download_count': {
            'type': 'integer',
        },        
        'note': {
            'type': 'number',
        },
        'xml_state': {
            'type': 'string',
        },
        'authors': {
            'type': 'list',
            'item': {
                'schema': {
                    'id': {
                        'type': 'integer'
                    },
                    'name': {
                        'type': 'string'
                    },
                },
            },
        },
        'versions': {
            'type': 'list',
            'item': {
                'schema': {
                    'num': {
                        'type': 'string'
                    },
                    'compatibility': {
                        'type': 'string'
                    },
                    'download_url': {
                        'type': 'string'
                    },
                    'stability': {
                        'type': 'string'
                    },
                },
            },
        },
        'descriptions': {
            'type': 'list',
            'item': {
                'schema': {
                    'lang': {
                        'type': 'string'
                    },
                    'short_descrption': {
                        'type': 'string'
                    },
                    'long_descrption': {
                        'type': 'string'
                    },
                },
            },
        },
        'required_offers': {
            'type': 'list'
        },
        'short_descrption': {
            'type': 'string'
        },
    }
}

tags = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'tag': {
            'type': 'string',
        },
        'lang': {
            'type': 'string',
            'minlength': 2,
            'maxlength': 3,
        }
    }
}

DOMAIN = {
    'registrationInfos': registrationInfos,
    'offers': offers,
    'plugins': plugins,
    'tags': tags,
}