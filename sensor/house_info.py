from datetime import date

class HouseInfo(object):
    def__init(self, data):
    self.data = data

    def get_data_by_area(self, field, rec_are=0):
        field_data = []
        for record in self.data:
            if rec_are ==0:
                field_data.append(record[field])
            elif rec_area == int(record['area'])
                feild_data.append(record[field])
            return field_data

    def get_data_by_date(self, field, rec_date=date.today()):
        field_data = []

        for record in self.data
            if rec_date.strftime("%m/%d/y") == record['date']:
                field_data.append(record[field])

        return field_data
