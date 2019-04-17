from object_packaging.field import Field
from object_packaging.my_database import create_pool


# 定义一个元类，控制model对象的创建
class ModelMetaClass(type):
    def __new__(cls, table_name, bases, attrs):
        if table_name == "Model":
            return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            # 保存类属性和列的映射关系到mappings字典中
            if isinstance(v, Field):
                mappings[k] = v  # 这样，这个mappings就存放了  属性名称和字段名称及列的名字
        for k in mappings.keys():
            attrs.pop(k)   # 只有在实例中才可以进行访问。也就是说使用类名.属性就不能访问了
        # 把表名转换为小写，表名就是类名
        # 这个处理略显粗糙，应该继续做一些健壮性的判断，比如ModelMetaClass 变成表名应该是model_meta_class
        attrs['__table__'] = table_name.lower()
        # 保存属性和列的映射关系，创建类时添加一个__mappings__类的属性
        attrs['__mappings__'] = mappings

        return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)



# 编写一个model子类，这个类用于被具体的model对象继承。 它实现了具体的增删改查方法
# 这样以后的每一个model就都有了这些方法
# 这里边我又继承了dict，那么也就是说这个Model也可以使用dict的方法

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError("这个Model没有这个属性，这个属性是%s" % item)

    def __setattr__(self, key, value):
        self[key] = value



    def insert(self, column_list, param_list):
        print("调用了insert方法")

        fields = []

        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        args = self.__check_params(param_list)

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(column_list), ','.join(args))

        res = self.__do_execute(sql)
        print(res)

    def __check_params(self, param_list):

        args = []
        #  insert into   ....   values "va"lue"
        for param in param_list:
            if "\"" in param:
                param = param.replace("\"", "\\\"")

            param = "\"" + param + "\""
            args.append(param)
        return args

    def __do_execute(self,sql):
        conn = create_pool()
        cur = conn.cursor()
        print(sql)

        if "select" in sql:
            cur.execute(sql)
            rs = cur.fetchall()
        else:
            rs = cur.execute(sql)

        conn.commit()
        cur.close()

        return rs
# 下边是作业

    # get  select

    def select(self, column_list, where_list):
        print("调用了select方法")
        args = []
        fields = []

        for k,v in self.__mappings__.items():
            fields.append(k)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        for key in where_list:
            args.append(key)

        sql = 'select %s from %s where %s' % (','.join(column_list), self.__table__, ' and '.join(args))

        res = self.__do_execute(sql)
        return res

    # update
    def update(self, set_column_list, where_list):
        print("调用了update方法")
        args = []
        fields = []


        for k,v in self.__mappings__.items():
            fields.append(k)

        for key in set_column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        for key in where_list:
            args.append(key)

        sql = 'update %s set %s where %s' % (self.__table__, ','.join(set_column_list), ' and '.join(args))

        print(sql)
        res = self.__do_execute(sql)

        return res




    # delete

    def delete(self, where_list):
        print("调用delete方法")
        args = []
        for key in where_list:
            args.append(key)

        sql = 'delete from %s where %s' % (self.__table__, ' and '.join(args))
        res = self.__do_execute(sql)

        return res

