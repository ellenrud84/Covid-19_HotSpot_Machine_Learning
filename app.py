import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from flask import Flask, jsonify, render_template
import pandas as pd
import json

app = Flask(__name__)

engine = create_engine("postgres://xebpvwdekstjxy:24a096ddb472f7eb9219c48ea89643aaf7a800ef199ba143a88add1036ac8e53@ec2-3-210-178-167.compute-1.amazonaws.com:5432/d5vu678447dkqu", echo=False)

conn = engine.connect()

#non looped sql queries

Demographics = pd.read_sql("select * from county_demographics",conn)

county_list_df = pd.read_sql("select distinct county_name from county_demographics",conn)

county_list= county_list_df['county_name']


#variables for sql loops

queries_cd=[]
queries_df=[]
queries_full=[]

result_cd =[]
parsed_cd = []

result_full =[]
parsed_full = []

for county in county_list:
    # queries_cd.append(pd.read_sql(f"select county_name, a.* a join county_demographics b on a.fips_code =b.fips_code where county_name ='{county}'",conn))
    queries_full.append(pd.read_sql(f"select county_name, a.* from county_daily_data a join county_demographics b on a.fips_code =b.fips_code where county_name ='{county}'",conn))
    queries_cd.append(pd.read_sql(f"select county_name, a.* from model_daily_data a join county_demographics b on a.fips_code =b.fips_code where county_name = '{county}'",conn))


# loop to jsonify cases and deaths

for x in range(len(queries_cd)):
    result_cd.append(queries_cd[x].to_json(orient='index'))
    parsed_cd.append(json.loads(result_cd[x]))


# loop to jsonify mobility

for x in range(len(queries_full)):
    result_full.append(queries_full[x].to_json(orient='index'))
    parsed_full.append(json.loads(result_full[x]))

queries = [Demographics]
result =[]
parsed = []

#jsonify demographics

for x in range(len(queries)):
    result.append(queries[x].to_json(orient='index'))
    parsed.append(json.loads(result[x]))

#start of routes

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Demographics")
def Demo():
    return jsonify(parsed[0])


## cases and deaths routes

@app.route(f'/{county_list[0]}')
def cd_0():
    return jsonify(parsed_cd[0])

@app.route(f"/{county_list[1]}")
def cd_1():
   return jsonify(parsed_cd[1])

@app.route(f"/{county_list[2]}")
def cd_2():
   return jsonify(parsed_cd[2])

@app.route(f"/{county_list[3]}")
def cd_3():
   return jsonify(parsed_cd[3])

@app.route(f"/{county_list[4]}")
def cd_4():
   return jsonify(parsed_cd[4])

@app.route(f'/{county_list[5]}')
def cd_5():
    return jsonify(parsed_cd[5])

@app.route(f'/{county_list[6]}')
def cd_6():
    return jsonify(parsed_cd[6])
@app.route(f'/{county_list[7]}')
def cd_7():
    return jsonify(parsed_cd[7])
@app.route(f'/{county_list[8]}')
def cd_8():
    return jsonify(parsed_cd[8])
@app.route(f'/{county_list[9]}')
def cd_9():
    return jsonify(parsed_cd[9])
@app.route(f'/{county_list[10]}')
def cd_10():
    return jsonify(parsed_cd[10])
@app.route(f'/{county_list[11]}')
def cd_11():
    return jsonify(parsed_cd[11])
@app.route(f'/{county_list[12]}')
def cd_12():
    return jsonify(parsed_cd[12])
@app.route(f'/{county_list[13]}')
def cd_13():
    return jsonify(parsed_cd[13])
@app.route(f'/{county_list[14]}')
def cd_14():
    return jsonify(parsed_cd[14])
@app.route(f'/{county_list[15]}')
def cd_15():
    return jsonify(parsed_cd[15])
@app.route(f'/{county_list[16]}')
def cd_16():
    return jsonify(parsed_cd[16])
@app.route(f'/{county_list[17]}')
def cd_17():
    return jsonify(parsed_cd[17])
@app.route(f'/{county_list[18]}')
def cd_18():
    return jsonify(parsed_cd[18])
@app.route(f'/{county_list[19]}')
def cd_19():
    return jsonify(parsed_cd[19])
@app.route(f'/{county_list[20]}')
def cd_20():
    return jsonify(parsed_cd[20])
@app.route(f'/{county_list[21]}')
def cd_21():
    return jsonify(parsed_cd[21])
@app.route(f'/{county_list[22]}')
def cd_22():
    return jsonify(parsed_cd[22])
@app.route(f'/{county_list[23]}')
def cd_23():
    return jsonify(parsed_cd[23])
@app.route(f'/{county_list[24]}')
def cd_24():
    return jsonify(parsed_cd[24])
@app.route(f'/{county_list[25]}')
def cd_25():
    return jsonify(parsed_cd[25])
@app.route(f'/{county_list[26]}')
def cd_26():
    return jsonify(parsed_cd[26])
@app.route(f'/{county_list[27]}')
def cd_27():
    return jsonify(parsed_cd[27])
@app.route(f'/{county_list[28]}')
def cd_28():
    return jsonify(parsed_cd[28])
@app.route(f'/{county_list[29]}')
def cd_29():
    return jsonify(parsed_cd[29])
@app.route(f'/{county_list[30]}')
def cd_30():
    return jsonify(parsed_cd[30])
@app.route(f'/{county_list[31]}')
def cd_31():
    return jsonify(parsed_cd[31])
@app.route(f'/{county_list[32]}')
def cd_32():
    return jsonify(parsed_cd[32])
@app.route(f'/{county_list[33]}')
def cd_33():
    return jsonify(parsed_cd[33])
@app.route(f'/{county_list[34]}')
def cd_34():
    return jsonify(parsed_cd[34])
@app.route(f'/{county_list[35]}')
def cd_35():
    return jsonify(parsed_cd[35])
@app.route(f'/{county_list[36]}')
def cd_36():
    return jsonify(parsed_cd[36])
@app.route(f'/{county_list[37]}')
def cd_37():
    return jsonify(parsed_cd[37])
@app.route(f'/{county_list[38]}')
def cd_38():
    return jsonify(parsed_cd[38])
@app.route(f'/{county_list[39]}')
def cd_39():
    return jsonify(parsed_cd[39])
@app.route(f'/{county_list[40]}')
def cd_40():
    return jsonify(parsed_cd[40])
@app.route(f'/{county_list[41]}')
def cd_41():
    return jsonify(parsed_cd[41])
@app.route(f'/{county_list[42]}')
def cd_42():
    return jsonify(parsed_cd[42])
@app.route(f'/{county_list[43]}')
def cd_43():
    return jsonify(parsed_cd[43])
@app.route(f'/{county_list[44]}')
def cd_44():
    return jsonify(parsed_cd[44])
@app.route(f'/{county_list[45]}')
def cd_45():
    return jsonify(parsed_cd[45])
@app.route(f'/{county_list[46]}')
def cd_46():
    return jsonify(parsed_cd[46])
@app.route(f'/{county_list[47]}')
def cd_47():
    return jsonify(parsed_cd[47])
@app.route(f'/{county_list[48]}')
def cd_48():
    return jsonify(parsed_cd[48])
@app.route(f'/{county_list[49]}')
def cd_49():
    return jsonify(parsed_cd[49])
@app.route(f'/{county_list[50]}')
def cd_50():
    return jsonify(parsed_cd[50])
@app.route(f'/{county_list[51]}')
def cd_51():
    return jsonify(parsed_cd[51])
@app.route(f'/{county_list[52]}')
def cd_52():
    return jsonify(parsed_cd[52])
@app.route(f'/{county_list[53]}')
def cd_53():
    return jsonify(parsed_cd[53])
@app.route(f'/{county_list[54]}')
def cd_54():
    return jsonify(parsed_cd[54])
@app.route(f'/{county_list[55]}')
def cd_55():
    return jsonify(parsed_cd[55])
@app.route(f'/{county_list[56]}')
def cd_56():
    return jsonify(parsed_cd[56])
@app.route(f'/{county_list[57]}')
def cd_57():
    return jsonify(parsed_cd[57])
@app.route(f'/{county_list[58]}')
def cd_58():
    return jsonify(parsed_cd[58])
@app.route(f'/{county_list[59]}')
def cd_59():
    return jsonify(parsed_cd[59])
@app.route(f'/{county_list[60]}')
def cd_60():
    return jsonify(parsed_cd[60])
@app.route(f'/{county_list[61]}')
def cd_61():
    return jsonify(parsed_cd[61])
@app.route(f'/{county_list[62]}')
def cd_62():
    return jsonify(parsed_cd[62])
@app.route(f'/{county_list[63]}')
def cd_63():
    return jsonify(parsed_cd[63])
@app.route(f'/{county_list[64]}')
def cd_64():
    return jsonify(parsed_cd[64])
@app.route(f'/{county_list[65]}')
def cd_65():
    return jsonify(parsed_cd[65])
@app.route(f'/{county_list[66]}')
def cd_66():
    return jsonify(parsed_cd[66])
@app.route(f'/{county_list[67]}')
def cd_67():
    return jsonify(parsed_cd[67])
@app.route(f'/{county_list[68]}')
def cd_68():
    return jsonify(parsed_cd[68])
@app.route(f'/{county_list[69]}')
def cd_69():
    return jsonify(parsed_cd[69])
@app.route(f'/{county_list[70]}')
def cd_70():
    return jsonify(parsed_cd[70])
@app.route(f'/{county_list[71]}')
def cd_71():
    return jsonify(parsed_cd[71])
@app.route(f'/{county_list[72]}')
def cd_72():
    return jsonify(parsed_cd[72])
@app.route(f'/{county_list[73]}')
def cd_73():
    return jsonify(parsed_cd[73])
@app.route(f'/{county_list[74]}')
def cd_74():
    return jsonify(parsed_cd[74])
@app.route(f'/{county_list[75]}')
def cd_75():
    return jsonify(parsed_cd[75])
@app.route(f'/{county_list[76]}')
def cd_76():
    return jsonify(parsed_cd[76])
@app.route(f'/{county_list[77]}')
def cd_77():
    return jsonify(parsed_cd[77])
@app.route(f'/{county_list[78]}')
def cd_78():
    return jsonify(parsed_cd[78])
@app.route(f'/{county_list[79]}')
def cd_79():
    return jsonify(parsed_cd[79])
@app.route(f'/{county_list[80]}')
def cd_80():
    return jsonify(parsed_cd[80])
@app.route(f'/{county_list[81]}')
def cd_81():
    return jsonify(parsed_cd[81])
@app.route(f'/{county_list[82]}')
def cd_82():
    return jsonify(parsed_cd[82])
@app.route(f'/{county_list[83]}')
def cd_83():
    return jsonify(parsed_cd[83])
@app.route(f'/{county_list[84]}')
def cd_84():
    return jsonify(parsed_cd[84])
@app.route(f'/{county_list[85]}')
def cd_85():
    return jsonify(parsed_cd[85])
@app.route(f'/{county_list[86]}')
def cd_86():
    return jsonify(parsed_cd[86])
@app.route(f'/{county_list[87]}')
def cd_87():
    return jsonify(parsed_cd[87])
@app.route(f'/{county_list[88]}')
def cd_88():
    return jsonify(parsed_cd[88])
@app.route(f'/{county_list[89]}')
def cd_89():
    return jsonify(parsed_cd[89])
@app.route(f'/{county_list[90]}')
def cd_90():
    return jsonify(parsed_cd[90])
@app.route(f'/{county_list[91]}')
def cd_91():
    return jsonify(parsed_cd[91])
@app.route(f'/{county_list[92]}')
def cd_92():
    return jsonify(parsed_cd[92])
@app.route(f'/{county_list[93]}')
def cd_93():
    return jsonify(parsed_cd[93])
@app.route(f'/{county_list[94]}')
def cd_94():
    return jsonify(parsed_cd[94])
@app.route(f'/{county_list[95]}')
def cd_95():
    return jsonify(parsed_cd[95])
@app.route(f'/{county_list[96]}')
def cd_96():
    return jsonify(parsed_cd[96])
@app.route(f'/{county_list[97]}')
def cd_97():
    return jsonify(parsed_cd[97])
@app.route(f'/{county_list[98]}')
def cd_98():
    return jsonify(parsed_cd[98])
@app.route(f'/{county_list[99]}')
def cd_99():
    return jsonify(parsed_cd[99])
@app.route(f'/{county_list[100]}')
def cd_100():
    return jsonify(parsed_cd[100])
@app.route(f'/{county_list[101]}')
def cd_101():
    return jsonify(parsed_cd[101])
@app.route(f'/{county_list[102]}')
def cd_102():
    return jsonify(parsed_cd[102])
@app.route(f'/{county_list[103]}')
def cd_103():
    return jsonify(parsed_cd[103])
@app.route(f'/{county_list[104]}')
def cd_104():
    return jsonify(parsed_cd[104])
@app.route(f'/{county_list[105]}')
def cd_105():
    return jsonify(parsed_cd[105])
@app.route(f'/{county_list[106]}')
def cd_106():
    return jsonify(parsed_cd[106])
@app.route(f'/{county_list[107]}')
def cd_107():
    return jsonify(parsed_cd[107])
@app.route(f'/{county_list[108]}')
def cd_108():
    return jsonify(parsed_cd[108])
@app.route(f'/{county_list[109]}')
def cd_109():
    return jsonify(parsed_cd[109])
@app.route(f'/{county_list[110]}')
def cd_110():
    return jsonify(parsed_cd[110])
@app.route(f'/{county_list[111]}')
def cd_111():
    return jsonify(parsed_cd[111])
@app.route(f'/{county_list[112]}')
def cd_112():
    return jsonify(parsed_cd[112])
@app.route(f'/{county_list[113]}')
def cd_113():
    return jsonify(parsed_cd[113])
@app.route(f'/{county_list[114]}')
def cd_114():
    return jsonify(parsed_cd[114])
@app.route(f'/{county_list[115]}')
def cd_115():
    return jsonify(parsed_cd[115])
@app.route(f'/{county_list[116]}')
def cd_116():
    return jsonify(parsed_cd[116])
@app.route(f'/{county_list[117]}')
def cd_117():
    return jsonify(parsed_cd[117])
@app.route(f'/{county_list[118]}')
def cd_118():
    return jsonify(parsed_cd[118])
@app.route(f'/{county_list[119]}')
def cd_119():
    return jsonify(parsed_cd[119])
@app.route(f'/{county_list[120]}')
def cd_120():
    return jsonify(parsed_cd[120])
@app.route(f'/{county_list[121]}')
def cd_121():
    return jsonify(parsed_cd[121])
@app.route(f'/{county_list[122]}')
def cd_122():
    return jsonify(parsed_cd[122])
@app.route(f'/{county_list[123]}')
def cd_123():
    return jsonify(parsed_cd[123])
@app.route(f'/{county_list[124]}')
def cd_124():
    return jsonify(parsed_cd[124])
@app.route(f'/{county_list[125]}')
def cd_125():
    return jsonify(parsed_cd[125])
@app.route(f'/{county_list[126]}')
def cd_126():
    return jsonify(parsed_cd[126])
@app.route(f'/{county_list[127]}')
def cd_127():
    return jsonify(parsed_cd[127])
@app.route(f'/{county_list[128]}')
def cd_128():
    return jsonify(parsed_cd[128])
@app.route(f'/{county_list[129]}')
def cd_129():
    return jsonify(parsed_cd[129])
@app.route(f'/{county_list[130]}')
def cd_130():
    return jsonify(parsed_cd[130])
@app.route(f'/{county_list[131]}')
def cd_131():
    return jsonify(parsed_cd[131])
@app.route(f'/{county_list[132]}')
def cd_132():
    return jsonify(parsed_cd[132])
@app.route(f'/{county_list[133]}')
def cd_133():
    return jsonify(parsed_cd[133])
@app.route(f'/{county_list[134]}')
def cd_134():
    return jsonify(parsed_cd[134])
@app.route(f'/{county_list[135]}')
def cd_135():
    return jsonify(parsed_cd[135])
@app.route(f'/{county_list[136]}')
def cd_136():
    return jsonify(parsed_cd[136])
@app.route(f'/{county_list[137]}')
def cd_137():
    return jsonify(parsed_cd[137])
@app.route(f'/{county_list[138]}')
def cd_138():
    return jsonify(parsed_cd[138])
@app.route(f'/{county_list[139]}')
def cd_139():
    return jsonify(parsed_cd[139])
@app.route(f'/{county_list[140]}')
def cd_140():
    return jsonify(parsed_cd[140])
@app.route(f'/{county_list[141]}')
def cd_141():
    return jsonify(parsed_cd[141])
@app.route(f'/{county_list[142]}')
def cd_142():
    return jsonify(parsed_cd[142])
@app.route(f'/{county_list[143]}')
def cd_143():
    return jsonify(parsed_cd[143])
@app.route(f'/{county_list[144]}')
def cd_144():
    return jsonify(parsed_cd[144])
@app.route(f'/{county_list[145]}')
def cd_145():
    return jsonify(parsed_cd[145])
@app.route(f'/{county_list[146]}')
def cd_146():
    return jsonify(parsed_cd[146])
@app.route(f'/{county_list[147]}')
def cd_147():
    return jsonify(parsed_cd[147])
@app.route(f'/{county_list[148]}')
def cd_148():
    return jsonify(parsed_cd[148])
@app.route(f'/{county_list[149]}')
def cd_149():
    return jsonify(parsed_cd[149])
@app.route(f'/{county_list[150]}')
def cd_150():
    return jsonify(parsed_cd[150])
@app.route(f'/{county_list[151]}')
def cd_151():
    return jsonify(parsed_cd[151])
@app.route(f'/{county_list[152]}')
def cd_152():
    return jsonify(parsed_cd[152])
@app.route(f'/{county_list[153]}')
def cd_153():
    return jsonify(parsed_cd[153])
@app.route(f'/{county_list[154]}')
def cd_154():
    return jsonify(parsed_cd[154])
@app.route(f'/{county_list[155]}')
def cd_155():
    return jsonify(parsed_cd[155])
@app.route(f'/{county_list[156]}')
def cd_156():
    return jsonify(parsed_cd[156])
@app.route(f'/{county_list[157]}')
def cd_157():
    return jsonify(parsed_cd[157])
@app.route(f'/{county_list[158]}')
def cd_158():
    return jsonify(parsed_cd[158])
@app.route(f'/{county_list[159]}')
def cd_159():
    return jsonify(parsed_cd[159])
@app.route(f'/{county_list[160]}')
def cd_160():
    return jsonify(parsed_cd[160])
@app.route(f'/{county_list[161]}')
def cd_161():
    return jsonify(parsed_cd[161])
@app.route(f'/{county_list[162]}')
def cd_162():
    return jsonify(parsed_cd[162])
@app.route(f'/{county_list[163]}')
def cd_163():
    return jsonify(parsed_cd[163])
@app.route(f'/{county_list[164]}')
def cd_164():
    return jsonify(parsed_cd[164])
@app.route(f'/{county_list[165]}')
def cd_165():
    return jsonify(parsed_cd[165])
@app.route(f'/{county_list[166]}')
def cd_166():
    return jsonify(parsed_cd[166])
@app.route(f'/{county_list[167]}')
def cd_167():
    return jsonify(parsed_cd[167])
@app.route(f'/{county_list[168]}')
def cd_168():
    return jsonify(parsed_cd[168])
@app.route(f'/{county_list[169]}')
def cd_169():
    return jsonify(parsed_cd[169])
@app.route(f'/{county_list[170]}')
def cd_170():
    return jsonify(parsed_cd[170])
@app.route(f'/{county_list[171]}')
def cd_171():
    return jsonify(parsed_cd[171])
@app.route(f'/{county_list[172]}')
def cd_172():
    return jsonify(parsed_cd[172])
@app.route(f'/{county_list[173]}')
def cd_173():
    return jsonify(parsed_cd[173])
@app.route(f'/{county_list[174]}')
def cd_174():
    return jsonify(parsed_cd[174])
@app.route(f'/{county_list[175]}')
def cd_175():
    return jsonify(parsed_cd[175])
@app.route(f'/{county_list[176]}')
def cd_176():
    return jsonify(parsed_cd[176])
@app.route(f'/{county_list[177]}')
def cd_177():
    return jsonify(parsed_cd[177])
@app.route(f'/{county_list[178]}')
def cd_178():
    return jsonify(parsed_cd[178])
@app.route(f'/{county_list[179]}')
def cd_179():
    return jsonify(parsed_cd[179])
@app.route(f'/{county_list[180]}')
def cd_180():
    return jsonify(parsed_cd[180])
@app.route(f'/{county_list[181]}')
def cd_181():
    return jsonify(parsed_cd[181])
@app.route(f'/{county_list[182]}')
def cd_182():
    return jsonify(parsed_cd[182])
@app.route(f'/{county_list[183]}')
def cd_183():
    return jsonify(parsed_cd[183])
@app.route(f'/{county_list[184]}')
def cd_184():
    return jsonify(parsed_cd[184])
@app.route(f'/{county_list[185]}')
def cd_185():
    return jsonify(parsed_cd[185])
@app.route(f'/{county_list[186]}')
def cd_186():
    return jsonify(parsed_cd[186])
@app.route(f'/{county_list[187]}')
def cd_187():
    return jsonify(parsed_cd[187])
@app.route(f'/{county_list[188]}')
def cd_188():
    return jsonify(parsed_cd[188])
@app.route(f'/{county_list[189]}')
def cd_189():
    return jsonify(parsed_cd[189])
@app.route(f'/{county_list[190]}')
def cd_190():
    return jsonify(parsed_cd[190])
@app.route(f'/{county_list[191]}')
def cd_191():
    return jsonify(parsed_cd[191])
@app.route(f'/{county_list[192]}')
def cd_192():
    return jsonify(parsed_cd[192])
@app.route(f'/{county_list[193]}')
def cd_193():
    return jsonify(parsed_cd[193])
@app.route(f'/{county_list[194]}')
def cd_194():
    return jsonify(parsed_cd[194])
@app.route(f'/{county_list[195]}')
def cd_195():
    return jsonify(parsed_cd[195])
@app.route(f'/{county_list[196]}')
def cd_196():
    return jsonify(parsed_cd[196])
@app.route(f'/{county_list[197]}')
def cd_197():
    return jsonify(parsed_cd[197])
@app.route(f'/{county_list[198]}')
def cd_198():
    return jsonify(parsed_cd[198])
@app.route(f'/{county_list[199]}')
def cd_199():
    return jsonify(parsed_cd[199])
@app.route(f'/{county_list[200]}')
def cd_200():
    return jsonify(parsed_cd[200])
@app.route(f'/{county_list[201]}')
def cd_201():
    return jsonify(parsed_cd[201])
@app.route(f'/{county_list[202]}')
def cd_202():
    return jsonify(parsed_cd[202])
@app.route(f'/{county_list[203]}')
def cd_203():
    return jsonify(parsed_cd[203])
@app.route(f'/{county_list[204]}')
def cd_204():
    return jsonify(parsed_cd[204])
@app.route(f'/{county_list[205]}')
def cd_205():
    return jsonify(parsed_cd[205])
@app.route(f'/{county_list[206]}')
def cd_206():
    return jsonify(parsed_cd[206])
@app.route(f'/{county_list[207]}')
def cd_207():
    return jsonify(parsed_cd[207])
@app.route(f'/{county_list[208]}')
def cd_208():
    return jsonify(parsed_cd[208])
@app.route(f'/{county_list[209]}')
def cd_209():
    return jsonify(parsed_cd[209])
@app.route(f'/{county_list[210]}')
def cd_210():
    return jsonify(parsed_cd[210])
@app.route(f'/{county_list[211]}')
def cd_211():
    return jsonify(parsed_cd[211])
@app.route(f'/{county_list[212]}')
def cd_212():
    return jsonify(parsed_cd[212])
@app.route(f'/{county_list[213]}')
def cd_213():
    return jsonify(parsed_cd[213])
@app.route(f'/{county_list[214]}')
def cd_214():
    return jsonify(parsed_cd[214])
@app.route(f'/{county_list[215]}')
def cd_215():
    return jsonify(parsed_cd[215])
@app.route(f'/{county_list[216]}')
def cd_216():
    return jsonify(parsed_cd[216])
@app.route(f'/{county_list[217]}')
def cd_217():
    return jsonify(parsed_cd[217])
@app.route(f'/{county_list[218]}')
def cd_218():
    return jsonify(parsed_cd[218])
@app.route(f'/{county_list[219]}')
def cd_219():
    return jsonify(parsed_cd[219])
@app.route(f'/{county_list[220]}')
def cd_220():
    return jsonify(parsed_cd[220])
@app.route(f'/{county_list[221]}')
def cd_221():
    return jsonify(parsed_cd[221])
@app.route(f'/{county_list[222]}')
def cd_222():
    return jsonify(parsed_cd[222])
@app.route(f'/{county_list[223]}')
def cd_223():
    return jsonify(parsed_cd[223])
@app.route(f'/{county_list[224]}')
def cd_224():
    return jsonify(parsed_cd[224])
@app.route(f'/{county_list[225]}')
def cd_225():
    return jsonify(parsed_cd[225])
@app.route(f'/{county_list[226]}')
def cd_226():
    return jsonify(parsed_cd[226])
@app.route(f'/{county_list[227]}')
def cd_227():
    return jsonify(parsed_cd[227])
@app.route(f'/{county_list[228]}')
def cd_228():
    return jsonify(parsed_cd[228])
@app.route(f'/{county_list[229]}')
def cd_229():
    return jsonify(parsed_cd[229])
@app.route(f'/{county_list[230]}')
def cd_230():
    return jsonify(parsed_cd[230])
@app.route(f'/{county_list[231]}')
def cd_231():
    return jsonify(parsed_cd[231])
@app.route(f'/{county_list[232]}')
def cd_232():
    return jsonify(parsed_cd[232])
@app.route(f'/{county_list[233]}')
def cd_233():
    return jsonify(parsed_cd[233])
@app.route(f'/{county_list[234]}')
def cd_234():
    return jsonify(parsed_cd[234])
@app.route(f'/{county_list[235]}')
def cd_235():
    return jsonify(parsed_cd[235])
@app.route(f'/{county_list[236]}')
def cd_236():
    return jsonify(parsed_cd[236])
@app.route(f'/{county_list[237]}')
def cd_237():
    return jsonify(parsed_cd[237])
@app.route(f'/{county_list[238]}')
def cd_238():
    return jsonify(parsed_cd[238])
@app.route(f'/{county_list[239]}')
def cd_239():
    return jsonify(parsed_cd[239])
@app.route(f'/{county_list[240]}')
def cd_240():
    return jsonify(parsed_cd[240])
@app.route(f'/{county_list[241]}')
def cd_241():
    return jsonify(parsed_cd[241])
@app.route(f'/{county_list[242]}')
def cd_242():
    return jsonify(parsed_cd[242])
@app.route(f'/{county_list[243]}')
def cd_243():
    return jsonify(parsed_cd[243])
@app.route(f'/{county_list[244]}')
def cd_244():
    return jsonify(parsed_cd[244])
@app.route(f'/{county_list[245]}')
def cd_245():
    return jsonify(parsed_cd[245])
@app.route(f'/{county_list[246]}')
def cd_246():
    return jsonify(parsed_cd[246])
@app.route(f'/{county_list[247]}')
def cd_247():
    return jsonify(parsed_cd[247])
@app.route(f'/{county_list[248]}')
def cd_248():
    return jsonify(parsed_cd[248])
@app.route(f'/{county_list[249]}')
def cd_249():
    return jsonify(parsed_cd[249])
@app.route(f'/{county_list[250]}')
def cd_250():
    return jsonify(parsed_cd[250])
@app.route(f'/{county_list[251]}')
def cd_251():
    return jsonify(parsed_cd[251])
@app.route(f'/{county_list[252]}')
def cd_252():
    return jsonify(parsed_cd[252])
@app.route(f'/{county_list[253]}')
def cd_253():
    return jsonify(parsed_cd[253])

## mobility data start

@app.route(f'/{county_list[0]}_Full')
def full_0():
    return jsonify(parsed_full[0])
@app.route(f'/{county_list[1]}_Full')
def full_1():
    return jsonify(parsed_full[1])
@app.route(f'/{county_list[2]}_Full')
def full_2():
    return jsonify(parsed_full[2])
@app.route(f'/{county_list[3]}_Full')
def full_3():
    return jsonify(parsed_full[3])
@app.route(f'/{county_list[4]}_Full')
def full_4():
    return jsonify(parsed_full[4])
@app.route(f'/{county_list[5]}_Full')
def full_5():
    return jsonify(parsed_full[5])
@app.route(f'/{county_list[6]}_Full')
def full_6():
    return jsonify(parsed_full[6])
@app.route(f'/{county_list[7]}_Full')
def full_7():
    return jsonify(parsed_full[7])
@app.route(f'/{county_list[8]}_Full')
def full_8():
    return jsonify(parsed_full[8])
@app.route(f'/{county_list[9]}_Full')
def full_9():
    return jsonify(parsed_full[9])
@app.route(f'/{county_list[10]}_Full')
def full_10():
    return jsonify(parsed_full[10])
@app.route(f'/{county_list[11]}_Full')
def full_11():
    return jsonify(parsed_full[11])
@app.route(f'/{county_list[12]}_Full')
def full_12():
    return jsonify(parsed_full[12])
@app.route(f'/{county_list[13]}_Full')
def full_13():
    return jsonify(parsed_full[13])
@app.route(f'/{county_list[14]}_Full')
def full_14():
    return jsonify(parsed_full[14])
@app.route(f'/{county_list[15]}_Full')
def full_15():
    return jsonify(parsed_full[15])
@app.route(f'/{county_list[16]}_Full')
def full_16():
    return jsonify(parsed_full[16])
@app.route(f'/{county_list[17]}_Full')
def full_17():
    return jsonify(parsed_full[17])
@app.route(f'/{county_list[18]}_Full')
def full_18():
    return jsonify(parsed_full[18])
@app.route(f'/{county_list[19]}_Full')
def full_19():
    return jsonify(parsed_full[19])
@app.route(f'/{county_list[20]}_Full')
def full_20():
    return jsonify(parsed_full[20])
@app.route(f'/{county_list[21]}_Full')
def full_21():
    return jsonify(parsed_full[21])
@app.route(f'/{county_list[22]}_Full')
def full_22():
    return jsonify(parsed_full[22])
@app.route(f'/{county_list[23]}_Full')
def full_23():
    return jsonify(parsed_full[23])
@app.route(f'/{county_list[24]}_Full')
def full_24():
    return jsonify(parsed_full[24])
@app.route(f'/{county_list[25]}_Full')
def full_25():
    return jsonify(parsed_full[25])
@app.route(f'/{county_list[26]}_Full')
def full_26():
    return jsonify(parsed_full[26])
@app.route(f'/{county_list[27]}_Full')
def full_27():
    return jsonify(parsed_full[27])
@app.route(f'/{county_list[28]}_Full')
def full_28():
    return jsonify(parsed_full[28])
@app.route(f'/{county_list[29]}_Full')
def full_29():
    return jsonify(parsed_full[29])
@app.route(f'/{county_list[30]}_Full')
def full_30():
    return jsonify(parsed_full[30])
@app.route(f'/{county_list[31]}_Full')
def full_31():
    return jsonify(parsed_full[31])
@app.route(f'/{county_list[32]}_Full')
def full_32():
    return jsonify(parsed_full[32])
@app.route(f'/{county_list[33]}_Full')
def full_33():
    return jsonify(parsed_full[33])
@app.route(f'/{county_list[34]}_Full')
def full_34():
    return jsonify(parsed_full[34])
@app.route(f'/{county_list[35]}_Full')
def full_35():
    return jsonify(parsed_full[35])
@app.route(f'/{county_list[36]}_Full')
def full_36():
    return jsonify(parsed_full[36])
@app.route(f'/{county_list[37]}_Full')
def full_37():
    return jsonify(parsed_full[37])
@app.route(f'/{county_list[38]}_Full')
def full_38():
    return jsonify(parsed_full[38])
@app.route(f'/{county_list[39]}_Full')
def full_39():
    return jsonify(parsed_full[39])
@app.route(f'/{county_list[40]}_Full')
def full_40():
    return jsonify(parsed_full[40])
@app.route(f'/{county_list[41]}_Full')
def full_41():
    return jsonify(parsed_full[41])
@app.route(f'/{county_list[42]}_Full')
def full_42():
    return jsonify(parsed_full[42])
@app.route(f'/{county_list[43]}_Full')
def full_43():
    return jsonify(parsed_full[43])
@app.route(f'/{county_list[44]}_Full')
def full_44():
    return jsonify(parsed_full[44])
@app.route(f'/{county_list[45]}_Full')
def full_45():
    return jsonify(parsed_full[45])
@app.route(f'/{county_list[46]}_Full')
def full_46():
    return jsonify(parsed_full[46])
@app.route(f'/{county_list[47]}_Full')
def full_47():
    return jsonify(parsed_full[47])
@app.route(f'/{county_list[48]}_Full')
def full_48():
    return jsonify(parsed_full[48])
@app.route(f'/{county_list[49]}_Full')
def full_49():
    return jsonify(parsed_full[49])
@app.route(f'/{county_list[50]}_Full')
def full_50():
    return jsonify(parsed_full[50])
@app.route(f'/{county_list[51]}_Full')
def full_51():
    return jsonify(parsed_full[51])
@app.route(f'/{county_list[52]}_Full')
def full_52():
    return jsonify(parsed_full[52])
@app.route(f'/{county_list[53]}_Full')
def full_53():
    return jsonify(parsed_full[53])
@app.route(f'/{county_list[54]}_Full')
def full_54():
    return jsonify(parsed_full[54])
@app.route(f'/{county_list[55]}_Full')
def full_55():
    return jsonify(parsed_full[55])
@app.route(f'/{county_list[56]}_Full')
def full_56():
    return jsonify(parsed_full[56])
@app.route(f'/{county_list[57]}_Full')
def full_57():
    return jsonify(parsed_full[57])
@app.route(f'/{county_list[58]}_Full')
def full_58():
    return jsonify(parsed_full[58])
@app.route(f'/{county_list[59]}_Full')
def full_59():
    return jsonify(parsed_full[59])
@app.route(f'/{county_list[60]}_Full')
def full_60():
    return jsonify(parsed_full[60])
@app.route(f'/{county_list[61]}_Full')
def full_61():
    return jsonify(parsed_full[61])
@app.route(f'/{county_list[62]}_Full')
def full_62():
    return jsonify(parsed_full[62])
@app.route(f'/{county_list[63]}_Full')
def full_63():
    return jsonify(parsed_full[63])
@app.route(f'/{county_list[64]}_Full')
def full_64():
    return jsonify(parsed_full[64])
@app.route(f'/{county_list[65]}_Full')
def full_65():
    return jsonify(parsed_full[65])
@app.route(f'/{county_list[66]}_Full')
def full_66():
    return jsonify(parsed_full[66])
@app.route(f'/{county_list[67]}_Full')
def full_67():
    return jsonify(parsed_full[67])
@app.route(f'/{county_list[68]}_Full')
def full_68():
    return jsonify(parsed_full[68])
@app.route(f'/{county_list[69]}_Full')
def full_69():
    return jsonify(parsed_full[69])
@app.route(f'/{county_list[70]}_Full')
def full_70():
    return jsonify(parsed_full[70])
@app.route(f'/{county_list[71]}_Full')
def full_71():
    return jsonify(parsed_full[71])
@app.route(f'/{county_list[72]}_Full')
def full_72():
    return jsonify(parsed_full[72])
@app.route(f'/{county_list[73]}_Full')
def full_73():
    return jsonify(parsed_full[73])
@app.route(f'/{county_list[74]}_Full')
def full_74():
    return jsonify(parsed_full[74])
@app.route(f'/{county_list[75]}_Full')
def full_75():
    return jsonify(parsed_full[75])
@app.route(f'/{county_list[76]}_Full')
def full_76():
    return jsonify(parsed_full[76])
@app.route(f'/{county_list[77]}_Full')
def full_77():
    return jsonify(parsed_full[77])
@app.route(f'/{county_list[78]}_Full')
def full_78():
    return jsonify(parsed_full[78])
@app.route(f'/{county_list[79]}_Full')
def full_79():
    return jsonify(parsed_full[79])
@app.route(f'/{county_list[80]}_Full')
def full_80():
    return jsonify(parsed_full[80])
@app.route(f'/{county_list[81]}_Full')
def full_81():
    return jsonify(parsed_full[81])
@app.route(f'/{county_list[82]}_Full')
def full_82():
    return jsonify(parsed_full[82])
@app.route(f'/{county_list[83]}_Full')
def full_83():
    return jsonify(parsed_full[83])
@app.route(f'/{county_list[84]}_Full')
def full_84():
    return jsonify(parsed_full[84])
@app.route(f'/{county_list[85]}_Full')
def full_85():
    return jsonify(parsed_full[85])
@app.route(f'/{county_list[86]}_Full')
def full_86():
    return jsonify(parsed_full[86])
@app.route(f'/{county_list[87]}_Full')
def full_87():
    return jsonify(parsed_full[87])
@app.route(f'/{county_list[88]}_Full')
def full_88():
    return jsonify(parsed_full[88])
@app.route(f'/{county_list[89]}_Full')
def full_89():
    return jsonify(parsed_full[89])
@app.route(f'/{county_list[90]}_Full')
def full_90():
    return jsonify(parsed_full[90])
@app.route(f'/{county_list[91]}_Full')
def full_91():
    return jsonify(parsed_full[91])
@app.route(f'/{county_list[92]}_Full')
def full_92():
    return jsonify(parsed_full[92])
@app.route(f'/{county_list[93]}_Full')
def full_93():
    return jsonify(parsed_full[93])
@app.route(f'/{county_list[94]}_Full')
def full_94():
    return jsonify(parsed_full[94])
@app.route(f'/{county_list[95]}_Full')
def full_95():
    return jsonify(parsed_full[95])
@app.route(f'/{county_list[96]}_Full')
def full_96():
    return jsonify(parsed_full[96])
@app.route(f'/{county_list[97]}_Full')
def full_97():
    return jsonify(parsed_full[97])
@app.route(f'/{county_list[98]}_Full')
def full_98():
    return jsonify(parsed_full[98])
@app.route(f'/{county_list[99]}_Full')
def full_99():
    return jsonify(parsed_full[99])
@app.route(f'/{county_list[100]}_Full')
def full_100():
    return jsonify(parsed_full[100])
@app.route(f'/{county_list[101]}_Full')
def full_101():
    return jsonify(parsed_full[101])
@app.route(f'/{county_list[102]}_Full')
def full_102():
    return jsonify(parsed_full[102])
@app.route(f'/{county_list[103]}_Full')
def full_103():
    return jsonify(parsed_full[103])
@app.route(f'/{county_list[104]}_Full')
def full_104():
    return jsonify(parsed_full[104])
@app.route(f'/{county_list[105]}_Full')
def full_105():
    return jsonify(parsed_full[105])
@app.route(f'/{county_list[106]}_Full')
def full_106():
    return jsonify(parsed_full[106])
@app.route(f'/{county_list[107]}_Full')
def full_107():
    return jsonify(parsed_full[107])
@app.route(f'/{county_list[108]}_Full')
def full_108():
    return jsonify(parsed_full[108])
@app.route(f'/{county_list[109]}_Full')
def full_109():
    return jsonify(parsed_full[109])
@app.route(f'/{county_list[110]}_Full')
def full_110():
    return jsonify(parsed_full[110])
@app.route(f'/{county_list[111]}_Full')
def full_111():
    return jsonify(parsed_full[111])
@app.route(f'/{county_list[112]}_Full')
def full_112():
    return jsonify(parsed_full[112])
@app.route(f'/{county_list[113]}_Full')
def full_113():
    return jsonify(parsed_full[113])
@app.route(f'/{county_list[114]}_Full')
def full_114():
    return jsonify(parsed_full[114])
@app.route(f'/{county_list[115]}_Full')
def full_115():
    return jsonify(parsed_full[115])
@app.route(f'/{county_list[116]}_Full')
def full_116():
    return jsonify(parsed_full[116])
@app.route(f'/{county_list[117]}_Full')
def full_117():
    return jsonify(parsed_full[117])
@app.route(f'/{county_list[118]}_Full')
def full_118():
    return jsonify(parsed_full[118])
@app.route(f'/{county_list[119]}_Full')
def full_119():
    return jsonify(parsed_full[119])
@app.route(f'/{county_list[120]}_Full')
def full_120():
    return jsonify(parsed_full[120])
@app.route(f'/{county_list[121]}_Full')
def full_121():
    return jsonify(parsed_full[121])
@app.route(f'/{county_list[122]}_Full')
def full_122():
    return jsonify(parsed_full[122])
@app.route(f'/{county_list[123]}_Full')
def full_123():
    return jsonify(parsed_full[123])
@app.route(f'/{county_list[124]}_Full')
def full_124():
    return jsonify(parsed_full[124])
@app.route(f'/{county_list[125]}_Full')
def full_125():
    return jsonify(parsed_full[125])
@app.route(f'/{county_list[126]}_Full')
def full_126():
    return jsonify(parsed_full[126])
@app.route(f'/{county_list[127]}_Full')
def full_127():
    return jsonify(parsed_full[127])
@app.route(f'/{county_list[128]}_Full')
def full_128():
    return jsonify(parsed_full[128])
@app.route(f'/{county_list[129]}_Full')
def full_129():
    return jsonify(parsed_full[129])
@app.route(f'/{county_list[130]}_Full')
def full_130():
    return jsonify(parsed_full[130])
@app.route(f'/{county_list[131]}_Full')
def full_131():
    return jsonify(parsed_full[131])
@app.route(f'/{county_list[132]}_Full')
def full_132():
    return jsonify(parsed_full[132])
@app.route(f'/{county_list[133]}_Full')
def full_133():
    return jsonify(parsed_full[133])
@app.route(f'/{county_list[134]}_Full')
def full_134():
    return jsonify(parsed_full[134])
@app.route(f'/{county_list[135]}_Full')
def full_135():
    return jsonify(parsed_full[135])
@app.route(f'/{county_list[136]}_Full')
def full_136():
    return jsonify(parsed_full[136])
@app.route(f'/{county_list[137]}_Full')
def full_137():
    return jsonify(parsed_full[137])
@app.route(f'/{county_list[138]}_Full')
def full_138():
    return jsonify(parsed_full[138])
@app.route(f'/{county_list[139]}_Full')
def full_139():
    return jsonify(parsed_full[139])
@app.route(f'/{county_list[140]}_Full')
def full_140():
    return jsonify(parsed_full[140])
@app.route(f'/{county_list[141]}_Full')
def full_141():
    return jsonify(parsed_full[141])
@app.route(f'/{county_list[142]}_Full')
def full_142():
    return jsonify(parsed_full[142])
@app.route(f'/{county_list[143]}_Full')
def full_143():
    return jsonify(parsed_full[143])
@app.route(f'/{county_list[144]}_Full')
def full_144():
    return jsonify(parsed_full[144])
@app.route(f'/{county_list[145]}_Full')
def full_145():
    return jsonify(parsed_full[145])
@app.route(f'/{county_list[146]}_Full')
def full_146():
    return jsonify(parsed_full[146])
@app.route(f'/{county_list[147]}_Full')
def full_147():
    return jsonify(parsed_full[147])
@app.route(f'/{county_list[148]}_Full')
def full_148():
    return jsonify(parsed_full[148])
@app.route(f'/{county_list[149]}_Full')
def full_149():
    return jsonify(parsed_full[149])
@app.route(f'/{county_list[150]}_Full')
def full_150():
    return jsonify(parsed_full[150])
@app.route(f'/{county_list[151]}_Full')
def full_151():
    return jsonify(parsed_full[151])
@app.route(f'/{county_list[152]}_Full')
def full_152():
    return jsonify(parsed_full[152])
@app.route(f'/{county_list[153]}_Full')
def full_153():
    return jsonify(parsed_full[153])
@app.route(f'/{county_list[154]}_Full')
def full_154():
    return jsonify(parsed_full[154])
@app.route(f'/{county_list[155]}_Full')
def full_155():
    return jsonify(parsed_full[155])
@app.route(f'/{county_list[156]}_Full')
def full_156():
    return jsonify(parsed_full[156])
@app.route(f'/{county_list[157]}_Full')
def full_157():
    return jsonify(parsed_full[157])
@app.route(f'/{county_list[158]}_Full')
def full_158():
    return jsonify(parsed_full[158])
@app.route(f'/{county_list[159]}_Full')
def full_159():
    return jsonify(parsed_full[159])
@app.route(f'/{county_list[160]}_Full')
def full_160():
    return jsonify(parsed_full[160])
@app.route(f'/{county_list[161]}_Full')
def full_161():
    return jsonify(parsed_full[161])
@app.route(f'/{county_list[162]}_Full')
def full_162():
    return jsonify(parsed_full[162])
@app.route(f'/{county_list[163]}_Full')
def full_163():
    return jsonify(parsed_full[163])
@app.route(f'/{county_list[164]}_Full')
def full_164():
    return jsonify(parsed_full[164])
@app.route(f'/{county_list[165]}_Full')
def full_165():
    return jsonify(parsed_full[165])
@app.route(f'/{county_list[166]}_Full')
def full_166():
    return jsonify(parsed_full[166])
@app.route(f'/{county_list[167]}_Full')
def full_167():
    return jsonify(parsed_full[167])
@app.route(f'/{county_list[168]}_Full')
def full_168():
    return jsonify(parsed_full[168])
@app.route(f'/{county_list[169]}_Full')
def full_169():
    return jsonify(parsed_full[169])
@app.route(f'/{county_list[170]}_Full')
def full_170():
    return jsonify(parsed_full[170])
@app.route(f'/{county_list[171]}_Full')
def full_171():
    return jsonify(parsed_full[171])
@app.route(f'/{county_list[172]}_Full')
def full_172():
    return jsonify(parsed_full[172])
@app.route(f'/{county_list[173]}_Full')
def full_173():
    return jsonify(parsed_full[173])
@app.route(f'/{county_list[174]}_Full')
def full_174():
    return jsonify(parsed_full[174])
@app.route(f'/{county_list[175]}_Full')
def full_175():
    return jsonify(parsed_full[175])
@app.route(f'/{county_list[176]}_Full')
def full_176():
    return jsonify(parsed_full[176])
@app.route(f'/{county_list[177]}_Full')
def full_177():
    return jsonify(parsed_full[177])
@app.route(f'/{county_list[178]}_Full')
def full_178():
    return jsonify(parsed_full[178])
@app.route(f'/{county_list[179]}_Full')
def full_179():
    return jsonify(parsed_full[179])
@app.route(f'/{county_list[180]}_Full')
def full_180():
    return jsonify(parsed_full[180])
@app.route(f'/{county_list[181]}_Full')
def full_181():
    return jsonify(parsed_full[181])
@app.route(f'/{county_list[182]}_Full')
def full_182():
    return jsonify(parsed_full[182])
@app.route(f'/{county_list[183]}_Full')
def full_183():
    return jsonify(parsed_full[183])
@app.route(f'/{county_list[184]}_Full')
def full_184():
    return jsonify(parsed_full[184])
@app.route(f'/{county_list[185]}_Full')
def full_185():
    return jsonify(parsed_full[185])
@app.route(f'/{county_list[186]}_Full')
def full_186():
    return jsonify(parsed_full[186])
@app.route(f'/{county_list[187]}_Full')
def full_187():
    return jsonify(parsed_full[187])
@app.route(f'/{county_list[188]}_Full')
def full_188():
    return jsonify(parsed_full[188])
@app.route(f'/{county_list[189]}_Full')
def full_189():
    return jsonify(parsed_full[189])
@app.route(f'/{county_list[190]}_Full')
def full_190():
    return jsonify(parsed_full[190])
@app.route(f'/{county_list[191]}_Full')
def full_191():
    return jsonify(parsed_full[191])
@app.route(f'/{county_list[192]}_Full')
def full_192():
    return jsonify(parsed_full[192])
@app.route(f'/{county_list[193]}_Full')
def full_193():
    return jsonify(parsed_full[193])
@app.route(f'/{county_list[194]}_Full')
def full_194():
    return jsonify(parsed_full[194])
@app.route(f'/{county_list[195]}_Full')
def full_195():
    return jsonify(parsed_full[195])
@app.route(f'/{county_list[196]}_Full')
def full_196():
    return jsonify(parsed_full[196])
@app.route(f'/{county_list[197]}_Full')
def full_197():
    return jsonify(parsed_full[197])
@app.route(f'/{county_list[198]}_Full')
def full_198():
    return jsonify(parsed_full[198])
@app.route(f'/{county_list[199]}_Full')
def full_199():
    return jsonify(parsed_full[199])
@app.route(f'/{county_list[200]}_Full')
def full_200():
    return jsonify(parsed_full[200])
@app.route(f'/{county_list[201]}_Full')
def full_201():
    return jsonify(parsed_full[201])
@app.route(f'/{county_list[202]}_Full')
def full_202():
    return jsonify(parsed_full[202])
@app.route(f'/{county_list[203]}_Full')
def full_203():
    return jsonify(parsed_full[203])
@app.route(f'/{county_list[204]}_Full')
def full_204():
    return jsonify(parsed_full[204])
@app.route(f'/{county_list[205]}_Full')
def full_205():
    return jsonify(parsed_full[205])
@app.route(f'/{county_list[206]}_Full')
def full_206():
    return jsonify(parsed_full[206])
@app.route(f'/{county_list[207]}_Full')
def full_207():
    return jsonify(parsed_full[207])
@app.route(f'/{county_list[208]}_Full')
def full_208():
    return jsonify(parsed_full[208])
@app.route(f'/{county_list[209]}_Full')
def full_209():
    return jsonify(parsed_full[209])
@app.route(f'/{county_list[210]}_Full')
def full_210():
    return jsonify(parsed_full[210])
@app.route(f'/{county_list[211]}_Full')
def full_211():
    return jsonify(parsed_full[211])
@app.route(f'/{county_list[212]}_Full')
def full_212():
    return jsonify(parsed_full[212])
@app.route(f'/{county_list[213]}_Full')
def full_213():
    return jsonify(parsed_full[213])
@app.route(f'/{county_list[214]}_Full')
def full_214():
    return jsonify(parsed_full[214])
@app.route(f'/{county_list[215]}_Full')
def full_215():
    return jsonify(parsed_full[215])
@app.route(f'/{county_list[216]}_Full')
def full_216():
    return jsonify(parsed_full[216])
@app.route(f'/{county_list[217]}_Full')
def full_217():
    return jsonify(parsed_full[217])
@app.route(f'/{county_list[218]}_Full')
def full_218():
    return jsonify(parsed_full[218])
@app.route(f'/{county_list[219]}_Full')
def full_219():
    return jsonify(parsed_full[219])
@app.route(f'/{county_list[220]}_Full')
def full_220():
    return jsonify(parsed_full[220])
@app.route(f'/{county_list[221]}_Full')
def full_221():
    return jsonify(parsed_full[221])
@app.route(f'/{county_list[222]}_Full')
def full_222():
    return jsonify(parsed_full[222])
@app.route(f'/{county_list[223]}_Full')
def full_223():
    return jsonify(parsed_full[223])
@app.route(f'/{county_list[224]}_Full')
def full_224():
    return jsonify(parsed_full[224])
@app.route(f'/{county_list[225]}_Full')
def full_225():
    return jsonify(parsed_full[225])
@app.route(f'/{county_list[226]}_Full')
def full_226():
    return jsonify(parsed_full[226])
@app.route(f'/{county_list[227]}_Full')
def full_227():
    return jsonify(parsed_full[227])
@app.route(f'/{county_list[228]}_Full')
def full_228():
    return jsonify(parsed_full[228])
@app.route(f'/{county_list[229]}_Full')
def full_229():
    return jsonify(parsed_full[229])
@app.route(f'/{county_list[230]}_Full')
def full_230():
    return jsonify(parsed_full[230])
@app.route(f'/{county_list[231]}_Full')
def full_231():
    return jsonify(parsed_full[231])
@app.route(f'/{county_list[232]}_Full')
def full_232():
    return jsonify(parsed_full[232])
@app.route(f'/{county_list[233]}_Full')
def full_233():
    return jsonify(parsed_full[233])
@app.route(f'/{county_list[234]}_Full')
def full_234():
    return jsonify(parsed_full[234])
@app.route(f'/{county_list[235]}_Full')
def full_235():
    return jsonify(parsed_full[235])
@app.route(f'/{county_list[236]}_Full')
def full_236():
    return jsonify(parsed_full[236])
@app.route(f'/{county_list[237]}_Full')
def full_237():
    return jsonify(parsed_full[237])
@app.route(f'/{county_list[238]}_Full')
def full_238():
    return jsonify(parsed_full[238])
@app.route(f'/{county_list[239]}_Full')
def full_239():
    return jsonify(parsed_full[239])
@app.route(f'/{county_list[240]}_Full')
def full_240():
    return jsonify(parsed_full[240])
@app.route(f'/{county_list[241]}_Full')
def full_241():
    return jsonify(parsed_full[241])
@app.route(f'/{county_list[242]}_Full')
def full_242():
    return jsonify(parsed_full[242])
@app.route(f'/{county_list[243]}_Full')
def full_243():
    return jsonify(parsed_full[243])
@app.route(f'/{county_list[244]}_Full')
def full_244():
    return jsonify(parsed_full[244])
@app.route(f'/{county_list[245]}_Full')
def full_245():
    return jsonify(parsed_full[245])
@app.route(f'/{county_list[246]}_Full')
def full_246():
    return jsonify(parsed_full[246])
@app.route(f'/{county_list[247]}_Full')
def full_247():
    return jsonify(parsed_full[247])
@app.route(f'/{county_list[248]}_Full')
def full_248():
    return jsonify(parsed_full[248])
@app.route(f'/{county_list[249]}_Full')
def full_249():
    return jsonify(parsed_full[249])
@app.route(f'/{county_list[250]}_Full')
def full_250():
    return jsonify(parsed_full[250])
@app.route(f'/{county_list[251]}_Full')
def full_251():
    return jsonify(parsed_full[251])
@app.route(f'/{county_list[252]}_Full')
def full_252():
    return jsonify(parsed_full[252])
@app.route(f'/{county_list[253]}_Full')
def full_253():
    return jsonify(parsed_full[253])




if __name__ == "__main__":
    app.run(debug=True)