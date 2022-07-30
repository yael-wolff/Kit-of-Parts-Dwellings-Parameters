class stage_C:
    def __init__(self, family_size=2, children_under_10=0):
        # size in squared meters
        self.size = 110
        self.bathroom_num = 2
        self.family_size = family_size
        self.children_under_10 = children_under_10
        self.children_over_10 = family_size - children_under_10 - 2
        #first floor
        self.living_room = 0
        self.bathroom1 = 0
        self.kitchen = 0
        self.dining_room = 0
        #second floor
        self.work_space = 0
        self.first_bedroom = 0
        #third_floor
        self.master_bedroom = 0
        self.bathroom2 = 0
        self.second_bedroom = 0

        self.rooms = ['living_room', 'bathroom1', 'kitchen', 'dining_room',
                      'work_space', 'first_bedroom', 'bathroom2', 'master_bedroom', 'second_bedroom']

    def not_crowded(self, metric='ACI'):
        '''
        find if the layout is crowded by different metrics
        :return: boolean, is crowded return True
        '''
        if metric == 'ACI':
            if (self.family_size > 4):
                return False
            else:
                return True
        elif metric == 'BBS':
            if (self.children_over_10 > 2):
                return False
            else:
                return True
        elif metric == 'ECI':
            if ((0.5*self.children_under_10+1+self.children_over_10)/2 > 1):
                return False
            else:
                return True

    def is_acc(self):
        return False