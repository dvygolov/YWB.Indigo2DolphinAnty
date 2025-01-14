import requests

class Auxiliary:
    def __init__(self, result):
        self.result = result

    def get_notes(self):
        try:
            notes = self.result['notes']
            return notes
        except KeyError:
            notes = ''
            return notes

    def get_proxy_type(self):
        if self.result['proxyType'] == 0:
            proxy_type = 'none';
        elif self.result['proxyType'] == 1:
            proxy_type = 'http'
        elif self.result['proxyType'] == 2:
            proxy_type = 'socks4'
        elif self.result['proxyType'] == 3:
            proxy_type = 'socks5'
        elif self.result['proxyType'] == 5:
            proxy_type = 'ssh'
        return proxy_type

    def get_proxy(self, proxy_type):
        if proxy_type == 'none':
            return {}
        return {
            'name': self.result['proxyHost'],
            'host': self.result['proxyHost'],
            'port': self.result['proxyPort'],
            'type': proxy_type,
            'login': self.result['proxyUser'],
            'password': self.result['proxyPass'],
        }

    def get_group_name(self, groups):
        for item in groups:
            if item['uuid'] == self.result['groupId']:
                result = item['name'] if 'name' in item else 'basic'
                return result

    def get_platform(self):
        if self.result['osType'] == 'mac':
            platform = 'macos'
            return platform
        elif self.result['osType'] == 'win':
            platform = 'windows'
            return platform

    def get_webgl2maximum(self):
        def get_webgl_param(result, param_name):
            for param in result['container']['webGlParams']:
                if param['name'] == param_name:
                    return param['value']
            for param in result['container']['webGl2Params']:
                if param['name'] == param_name:
                    return param['value']

        return {
            "MAX_SAMPLES": get_webgl_param(self.result, 'MAX_SAMPLES'),
            "MAX_DRAW_BUFFERS": get_webgl_param(self.result, 'MAX_DRAW_BUFFERS'),
            "MAX_TEXTURE_SIZE": get_webgl_param(self.result, 'MAX_TEXTURE_SIZE'),
            "MAX_ELEMENT_INDEX": get_webgl_param(self.result, 'MAX_ELEMENT_INDEX'),
            "MAX_VIEWPORT_DIMS": get_webgl_param(self.result, 'MAX_VIEWPORT_DIMS'),
            "MAX_VERTEX_ATTRIBS": get_webgl_param(self.result, 'MAX_VERTEX_ATTRIBS'),
            "MAX_3D_TEXTURE_SIZE": get_webgl_param(self.result, 'MAX_3D_TEXTURE_SIZE'),
            "MAX_VARYING_VECTORS": get_webgl_param(self.result, 'MAX_VARYING_VECTORS'),
            "MAX_ELEMENTS_INDICES": get_webgl_param(self.result, 'MAX_ELEMENTS_INDICES'),
            "MAX_TEXTURE_LOD_BIAS": get_webgl_param(self.result, 'MAX_TEXTURE_LOD_BIAS'),
            "MAX_COLOR_ATTACHMENTS": get_webgl_param(self.result, 'MAX_COLOR_ATTACHMENTS'),
            "MAX_ELEMENTS_VERTICES": get_webgl_param(self.result, 'MAX_ELEMENTS_VERTICES'),
            "MAX_RENDERBUFFER_SIZE": get_webgl_param(self.result, 'MAX_RENDERBUFFER_SIZE'),
            "MAX_UNIFORM_BLOCK_SIZE": get_webgl_param(self.result, 'MAX_UNIFORM_BLOCK_SIZE'),
            "MAX_VARYING_COMPONENTS": get_webgl_param(self.result, 'MAX_VARYING_COMPONENTS'),
            "MAX_TEXTURE_IMAGE_UNITS": get_webgl_param(self.result, 'MAX_TEXTURE_IMAGE_UNITS'),
            "MAX_ARRAY_TEXTURE_LAYERS": get_webgl_param(self.result, 'MAX_ARRAY_TEXTURE_LAYERS'),
            "MAX_PROGRAM_TEXEL_OFFSET": get_webgl_param(self.result, 'MAX_PROGRAM_TEXEL_OFFSET'),
            "MIN_PROGRAM_TEXEL_OFFSET": get_webgl_param(self.result, 'MIN_PROGRAM_TEXEL_OFFSET'),
            "MAX_CUBE_MAP_TEXTURE_SIZE": get_webgl_param(self.result, 'MAX_CUBE_MAP_TEXTURE_SIZE'),
            "MAX_VERTEX_UNIFORM_BLOCKS": get_webgl_param(self.result, 'MAX_VERTEX_UNIFORM_BLOCKS'),
            "MAX_VERTEX_UNIFORM_VECTORS": get_webgl_param(self.result, 'MAX_VERTEX_UNIFORM_VECTORS'),
            "MAX_COMBINED_UNIFORM_BLOCKS": get_webgl_param(self.result, 'MAX_COMBINED_UNIFORM_BLOCKS'),
            "MAX_FRAGMENT_UNIFORM_BLOCKS": get_webgl_param(self.result, 'MAX_FRAGMENT_UNIFORM_BLOCKS'),
            "MAX_UNIFORM_BUFFER_BINDINGS": get_webgl_param(self.result, 'MAX_UNIFORM_BUFFER_BINDINGS'),
            "MAX_FRAGMENT_UNIFORM_VECTORS": get_webgl_param(self.result, 'MAX_FRAGMENT_UNIFORM_VECTORS'),
            "MAX_VERTEX_OUTPUT_COMPONENTS": get_webgl_param(self.result, 'MAX_VERTEX_OUTPUT_COMPONENTS'),
            "MAX_FRAGMENT_INPUT_COMPONENTS": get_webgl_param(self.result, 'MAX_FRAGMENT_INPUT_COMPONENTS'),
            "MAX_VERTEX_UNIFORM_COMPONENTS": get_webgl_param(self.result, 'MAX_VERTEX_UNIFORM_COMPONENTS'),
            "MAX_VERTEX_TEXTURE_IMAGE_UNITS": get_webgl_param(self.result, 'MAX_VERTEX_TEXTURE_IMAGE_UNITS'),
            "MAX_FRAGMENT_UNIFORM_COMPONENTS": get_webgl_param(self.result, 'MAX_FRAGMENT_UNIFORM_COMPONENTS'),
            "UNIFORM_BUFFER_OFFSET_ALIGNMENT": get_webgl_param(self.result, 'UNIFORM_BUFFER_OFFSET_ALIGNMENT'),
            "MAX_COMBINED_TEXTURE_IMAGE_UNITS": get_webgl_param(self.result, 'MAX_COMBINED_TEXTURE_IMAGE_UNITS'),
            "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": get_webgl_param(self.result,
                                                                      'MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS'),
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": get_webgl_param(self.result,
                                                                       'MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS'),
            "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": get_webgl_param(self.result,
                                                                        'MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS'),
            "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": get_webgl_param(self.result,
                                                                          'MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS'),
            "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": get_webgl_param(self.result,
                                                                             'MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS')
        }
