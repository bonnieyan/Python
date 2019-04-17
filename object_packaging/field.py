
# 我们来定义Field类，用来保存数据库表的字段名称和字段类型
class Field(object):
    def __init__(self, column_name, column_type):
        self.column_name = column_name
        self.column_type = column_type

class StringField(Field):
    def __init__(self, column_name):
        super(StringField,self).__init__(column_name, 'varchar(200)')


class IntegerField(Field):
    def __init__(self, column_name):
        super(IntegerField, self).__init__(column_name, 'bigint')


class TextField(Field):
    def __init__(self, column_name):
        super(TextField, self).__init__(column_name, 'text')



# 第二种写法
class DataField(Field):
    def __init__(self, column_name, column_type):
        super(DataField, self).__init__(column_name, column_type)


