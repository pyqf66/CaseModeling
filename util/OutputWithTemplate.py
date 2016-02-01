# -*- coding:utf-8 -*-
import xlrd
import xlwt
from util.TimeStamp import TimeStamp

from util.logger import logger


class OutputWithTemplate(object):
    def output_with_excel(self, template_file, sheet_count,data_list):
        '''
        :param template_file: 模板文件路径
        :param sheet_count: 模板文件容sheet的个数，比如5个sheet页通过这个参数可以指定就用3个
        :param data_list: 数据list，其中包含sheet页list，表头list，数据list
        本方法中均使用list进行数据操作
        '''
        try:
            data = xlrd.open_workbook(template_file)
            sheet_name = data.sheet_names()
            sheet_list = list()
            # 将模板文件sheet对象存入sheet_list列表
            for i in range(sheet_count):
                sheet_list.append(data.sheets()[i])
            template_data_list = list()
            # 将模板文件每个sheet的数据list存入tempLate_data_list列表
            for i_sheet in sheet_list:
                template_data_list.append(i_sheet.row_values(0))
            output_file = xlwt.Workbook()
            #字体设定
            font=xlwt.Font()
            font.bold=True
            #边框设定
            borders=xlwt.Borders()
            borders.left=1
            borders.right=1
            borders.top=1
            borders.bottom=1
            #背景色设定
            backcolor=xlwt.Pattern()
            backcolor.pattern=xlwt.Pattern.SOLID_PATTERN
            backcolor.pattern_fore_colour=5
            style=xlwt.XFStyle()
            style.font=font
            style.borders=borders
            style.pattern=backcolor
            output_file_sheet_list = list()
            # 输出文件添加sheet并给予标题,对象存入output_file_sheet_list列表
            for j in range(sheet_count):
                output_file_sheet_list.append(output_file.add_sheet(sheet_name[j],cell_overwrite_ok=True))
            # j_sheet_num为sheet页的索引
            for j_sheet_num in range(len(sheet_list)):
                # j_sheet_row_index为模板文件template_dataList的索引
                for j_sheet_row_index in range(len(template_data_list[j_sheet_num])):
                    output_file_sheet_list[j_sheet_num].write(0, j_sheet_row_index,
                                                              template_data_list[j_sheet_num][j_sheet_row_index],style)

            #插数据
            for data_num in range(len(data_list[0])):
                logger.debug(data_num)
                logger.debug(data_list)
                output_file_sheet_list[int(data_list[0][data_num])-1].write(data_num+1,int(data_list[1][data_num])-1,data_list[2][data_num])

            output_file.save(str(TimeStamp.time_stamp()) + ".xls")


        except:
            logger.exception("发现错误")