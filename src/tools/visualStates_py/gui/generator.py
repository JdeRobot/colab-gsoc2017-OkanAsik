
class Generator():

    def __init__(self):
        pass


    def generateCfg(self, cfgStr):
        for cfg in self.configs:
            interface = cfg['interface']
            if interface == 'ArDroneExtra':
                interface = 'Extra'

            proxyName = cfg['proxyName']
            if len(proxyName) == 0:
                proxyName = cfg['interface']

            cfgStr.append('automata.')
            cfgStr.append(cfg['name'])
            cfgStr.append('.Proxy=')
            cfgStr.append(proxyName)
            cfgStr.append(':default -h ')
            cfgStr.append(cfg['ip'])
            cfgStr.append(' -p ')
            cfgStr.append(str(cfg['port']))
            cfgStr.append('\n')

        return cfgStr


    def generateUserMethods(self, methodStr):
        for state in self.states:
            methodStr.append(state.getMethods())
            methodStr.append('\n')
        return methodStr