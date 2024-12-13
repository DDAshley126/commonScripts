from models.Models import Order
from models.Models import db


def test_api():
    data = db.session.query(Order).filter(Order.year_and_month == '2024年10月').all()
    return query2dict(data)


def query2dict(model_list):
    if isinstance(model_list, list):    # 如果传入的参数是一个list类型的，说明是使用的all()的方式查询的
        if isinstance(model_list[0], db.Model):     # 这种方式是获得的整个对象  相当于 select * from table
            lst = []
            for model in model_list:
                dic = {}
                for col in model.__table__.columns:
                    dic[col.name] = getattr(model, col.name)
                lst.append(dic)
            return lst
        else:   # 这种方式获得了数据库中的个别字段  相当于select id,name from table
            lst = []
            for result in model_list:
                lst.append([dict(zip(result.keys, r)) for r in result])
            return lst
    else:   # 不是list,说明是用的get() 或者 first()查询的，得到的结果是一个对象
        if isinstance(model_list, db.Model):    # 这种方式是获得的整个对象  相当于 select * from table limit=1
            dic = {}
            for col in model_list.__table__.columns:
                dic[col.name] = getattr(model_list, col.name)
            return dic
        else:   # 这种方式获得了数据库中的个别字段  相当于select id,name from table limit = 1
            return dict(zip(model_list.keys(), model_list))