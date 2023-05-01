# NTU VGRADRECRUIT EMPLOYERS LIST

import re
from bs4 import BeautifulSoup
import csv

html_doc = """
<div class="empList">
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_0" value="EYI9WQGSMNU4M6XY0128">
              <label class="selection" for="employersFav_0">NTU Career &amp; Attachment Office</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_1" value="EC6UWU88XELJQSLKKY50">
              <label class="selection" for="employersFav_1">CGG SERVICES (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_2" value="DJ4NLJF89ACJ9RSB9UM3">
              <label class="selection" for="employersFav_2">YT AUTOMATION SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_3" value="SDJJAEOMBD15XK02Q8Q9">
              <label class="selection" for="employersFav_3">REPUBLIC OF SINGAPORE AIR FORCE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_4" value="B9XB860K7RFRMPZYZPJ2">
              <label class="selection" for="employersFav_4">ESG TECH EVENTS PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_5" value="SSHJ399UE2LL6P4RMAU2">
              <label class="selection" for="employersFav_5">MARQUEE SEMICONDUCTOR SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_6" value="SYC4MDH7GK8OASPACYE7">
              <label class="selection" for="employersFav_6">VFLOWTECH PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_7" value="LACJLE8TOSCJKAKKZBN0">
              <label class="selection" for="employersFav_7">COSTELLO MEDICAL SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_8" value="M48MQ5T6O23218HRDYZ4">
              <label class="selection" for="employersFav_8">TOTALENERGIES TRADING ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_9" value="E88WI2Y47M2RIYN0SAT3">
              <label class="selection" for="employersFav_9">VISIBILITY DESIGN PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_10" value="3LJKFBMM9PAJTP3OZG02">
              <label class="selection" for="employersFav_10">THE DIGITAL AND INTELLIGENCE SERVICE (DIS)</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_11" value="AHMN6L4QKEHF12PIDJC7">
              <label class="selection" for="employersFav_11">KANGAROO LEARNING CENTER PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_12" value="U1Z8QK84JI4QB8SDSQF0">
              <label class="selection" for="employersFav_12">SINGAPORE CIVIL DEFENCE FORCE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_13" value="TQLC60H2DRW2K9QGIQS8">
              <label class="selection" for="employersFav_13">RSM</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_14" value="544JLSC1XTLH3BZJ75O7">
              <label class="selection" for="employersFav_14">LAND TRANSPORT AUTHORITY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_15" value="32BKX7MHD6MPH19J7R36">
              <label class="selection" for="employersFav_15">COLLABERA DIGITAL</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_16" value="CD7SA6QAFGY079A93KU2">
              <label class="selection" for="employersFav_16">ONE DASH 22 PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_17" value="9829HKRS05OJ7KSLY7U8">
              <label class="selection" for="employersFav_17">YONYOU SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_18" value="D8CEDY7X4O2J25ZXYN33">
              <label class="selection" for="employersFav_18">BERNHARD SCHULTE SHIPMANAGEMENT (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_19" value="ZN2SC27OO19O0AD8X515">
              <label class="selection" for="employersFav_19">TATA CONSULTANCY SERVICES ASIA PACIFIC PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_20" value="WR0MGZA7FKY41EQZSRL4">
              <label class="selection" for="employersFav_20">SYNPULSE SINGAPORE PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_21" value="JWCCU8Y7Q7GBUMLIP4N8">
              <label class="selection" for="employersFav_21">EDUCLAAS GLOBAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_22" value="6H9K9SDEZC0N86YKSZI6">
              <label class="selection" for="employersFav_22">SYSTEMS ON SILICON MANUFACTURING COMPANY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_23" value="UFUAR7ADFD38FKM7H3Q6">
              <label class="selection" for="employersFav_23">ACCURACY SINGAPORE CORPORATE ADVISORY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_24" value="6FS4P3B4KKXKY27XPJN3">
              <label class="selection" for="employersFav_24">PKF-CAP LLP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_25" value="FDUMTI6TCWK04D2BLWN5">
              <label class="selection" for="employersFav_25">ERNST &amp; YOUNG SOLUTIONS LLP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_26" value="KFOEEQ20MU59TYPX22G3">
              <label class="selection" for="employersFav_26">SIMPLE SOLUTION SYSTEMS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_27" value="IK5FBFXLWTLDWAMW9NB1">
              <label class="selection" for="employersFav_27">BW OFFSHORE HOLDINGS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_28" value="K0GL9TPF0WP9UMIPR708">
              <label class="selection" for="employersFav_28">ATLAS COPCO (SEA) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_29" value="I1SBGQ5MPAFKWZO83TL7">
              <label class="selection" for="employersFav_29">MINISTRY OF DEFENCE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_30" value="D935QCXQ39D70HYSSZX9">
              <label class="selection" for="employersFav_30">INMAGINE LAB PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_31" value="TKQ43IBZLHOQWMZ1RN47">
              <label class="selection" for="employersFav_31">CENTURY COMMODITIES SOLUTION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_32" value="F5OUWWGW1QGK37IKFSL7">
              <label class="selection" for="employersFav_32">SINGAPORE HAI DI LAO DINING PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_33" value="8AQ8SSMYZB17SWGOQP64">
              <label class="selection" for="employersFav_33">JURONG ENGINEERING LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_34" value="K5N5LE76NEG1H0JHF127">
              <label class="selection" for="employersFav_34">QIAN HU CORPORATION LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_35" value="T7L5ACCJFS9YMKUCORQ9">
              <label class="selection" for="employersFav_35">BAKER TILLY TFW LLP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_36" value="KJMZ5TTY408GP2NXUTF1">
              <label class="selection" for="employersFav_36">AIBEL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_37" value="9L11FRD9UPUEY09B7WJ2">
              <label class="selection" for="employersFav_37">UNITED MICROELECTRONICS CORPORATION (SINGAPORE BRANCH)</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_38" value="EGF6L9KBJOU3BR5SN3L2">
              <label class="selection" for="employersFav_38">Singapore Police Force</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_39" value="I2NACGS6KQE7GE3CLEJ2">
              <label class="selection" for="employersFav_39">TRANS EUROKARS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_40" value="1G3HENWALFQ96H69FO91">
              <label class="selection" for="employersFav_40">BENG HOCK MECHANICAL ENGINEERING PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_41" value="WUJNRLYCI5GK0APOPAA7">
              <label class="selection" for="employersFav_41">HUAWEI SINGAPORE RESEARCH CENTRE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_42" value="NNB11DER9KIF4B3GZ5A1">
              <label class="selection" for="employersFav_42">NATIONAL TRADES UNION CONGRESS</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_43" value="CP4E6YJ08A6Q2M0MGW45">
              <label class="selection" for="employersFav_43">WIZVISION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_44" value="T7TWZD41YNL6XK8EA6J6">
              <label class="selection" for="employersFav_44">PACIFIC REFRESHMENTS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_45" value="HZO3553DHD2RJMXX7NI6">
              <label class="selection" for="employersFav_45">SCIENCE STUDIOS LEARNING CENTRE PTE LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_46" value="L29XWYZGRKH5BRWYOC39">
              <label class="selection" for="employersFav_46">NCS GROUP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_47" value="ZTRBA6UB4PTOD85UZP04">
              <label class="selection" for="employersFav_47">D-SIMLAB TECHNOLOGIES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_48" value="STTBJY0U9JCU2F4D8X71">
              <label class="selection" for="employersFav_48">SPEEDCARGO TECHNOLOGIES PTE. LTD. </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_49" value="8T2I1K3FU3X20WZ96ET4">
              <label class="selection" for="employersFav_49">OLDENDORFF CARRIERS (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_50" value="ABM0P5FZT3G9WDJRDAM8">
              <label class="selection" for="employersFav_50">PURITEK COMPANY LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_51" value="3AAAXHOGOAABNN0647D7">
              <label class="selection" for="employersFav_51">TERRENUS ENERGY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_52" value="NS0K77C11XJ14OU96A91">
              <label class="selection" for="employersFav_52">DEZIGN FORMAT PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_53" value="Z9OMXER7ZJFWC8G0Q0P0">
              <label class="selection" for="employersFav_53">SINGAPORE GENERAL HOSPITAL </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_54" value="J9KDMMQQUZ76P7RXNFH9">
              <label class="selection" for="employersFav_54">THE SOFTWARE PRACTICE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_55" value="CSWE11G1Z36AWB1ZTT36">
              <label class="selection" for="employersFav_55">SYSTEMENGINEER360 PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_56" value="ULFYA9WJ309E12NX4KQ9">
              <label class="selection" for="employersFav_56">KEYENCE SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_57" value="TDG71DCDMFFLB1FN7TN0">
              <label class="selection" for="employersFav_57">ROVISYS ASIA COMPANY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_58" value="AUEQPWNMHJ62P899TWS1">
              <label class="selection" for="employersFav_58">MOORE STEPHENS LLP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_59" value="90NSX5BE4W3ITPCJSRD7">
              <label class="selection" for="employersFav_59">ALSTON EDUCATION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_60" value="4FAIHSWBJ4X6JC2OFEF9">
              <label class="selection" for="employersFav_60">IDEA INK ILLUSTRATIONS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_61" value="XEID62W3CBXC3XKQQ9H5">
              <label class="selection" for="employersFav_61">STALFORD EDUCATION GROUP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_62" value="NFDM8JQJXD53Y8HSH8S9">
              <label class="selection" for="employersFav_62">ST ENGINEERING </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_63" value="SACWEPW3PFSDBLAXLQL5">
              <label class="selection" for="employersFav_63">PANASONIC R&amp;D CENTER SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_64" value="UTLSLXJ481YU3LJ29N88">
              <label class="selection" for="employersFav_64">REC SOLAR PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_65" value="A5YQQO0HQWQ9SO2T4BJ9">
              <label class="selection" for="employersFav_65">DHL GLOBAL FORWARDING SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_66" value="ONK13IG37ML27FJYPH93">
              <label class="selection" for="employersFav_66">CENTRE FOR STRATEGIC INFOCOMM TECHNOLOGIES</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_67" value="CN1BPQ3Y0BLQ6DQEHX19">
              <label class="selection" for="employersFav_67">MUJIN,INC.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_68" value="0Z3H2TST8JZK46GQTZC7">
              <label class="selection" for="employersFav_68">MINISTRY OF EDUCATION</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_69" value="XT6T52P6I469O7QEU1X0">
              <label class="selection" for="employersFav_69">HALLIBURTON</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_70" value="PEA1ETMF0SLID89PZ0J7">
              <label class="selection" for="employersFav_70">INFOSYS LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_71" value="KSQEQMIX70XQM431R9X2">
              <label class="selection" for="employersFav_71">SCHENKER SINGAPORE (PTE) LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_72" value="6M660JNQI4X9008QS8F7">
              <label class="selection" for="employersFav_72">SINGAPORE CUSTOMS</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_73" value="3SLBFUHRXGMZZ65URY87">
              <label class="selection" for="employersFav_73">KEYSTONE CABLE (S) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_74" value="5BWNHIH0MJ1HJA76JMS4">
              <label class="selection" for="employersFav_74">IDEMIA SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_75" value="10M392F4YSXIZRJIZ2B8">
              <label class="selection" for="employersFav_75">NUSTAR TECHNOLOGIES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_76" value="SRNOKTAEBU3KZJJH7EC4">
              <label class="selection" for="employersFav_76">FOXCONN INDUSTRIAL INTERNET - CLOUD NETWORK TECHNOLOGY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_77" value="TU6RKP0DMK06QB97IQI3">
              <label class="selection" for="employersFav_77">TRAMES PRIVATE LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_78" value="JB633F8S0TZ4YA2R5AH3">
              <label class="selection" for="employersFav_78">INLAND REVENUE AUTHORITY OF SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_79" value="NNCHBUS4CUWITMGLT2X3">
              <label class="selection" for="employersFav_79">CONVERGINT SINGAPROE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_80" value="DH9HWG3YRGIUFFNCPTO7">
              <label class="selection" for="employersFav_80">CONTINENTAL AUTOMOTIVE SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_81" value="D6AOPXAJ9SHQ0NFYAY64">
              <label class="selection" for="employersFav_81">SNK GAMES SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_82" value="NSIL0N0WOY6ZY3L04IB2">
              <label class="selection" for="employersFav_82">ASM FRONT-END MANUFACTURING SERVICES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_83" value="H3NAPF60KAKZD1JIXK17">
              <label class="selection" for="employersFav_83">SINGAPORE ARMED FORCES (ARMY)</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_84" value="I78YY0AHI0JD2H7OUAY9">
              <label class="selection" for="employersFav_84">MINISTRY OF HOME AFFAIRS</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_85" value="SORNGAYGP347N6FG89H5">
              <label class="selection" for="employersFav_85">PEC LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_86" value="1LUNOCD8S8WRSQZMDB24">
              <label class="selection" for="employersFav_86">ALTRAD SERVICES SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_87" value="2UE6NCRGOF7IF10KD9A3">
              <label class="selection" for="employersFav_87">COGNIZANT TECHNOLOGY SOLUTIONS ASIA</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_88" value="WS1WFOOQ7EG1XQP9Y6O7">
              <label class="selection" for="employersFav_88">NOVI HEALTH</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_89" value="R9O1ST6EEIBGMJZOBJK0">
              <label class="selection" for="employersFav_89">HCL TECHNOLOGIES SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_90" value="AM5IMQSN63QKK5BRUIE3">
              <label class="selection" for="employersFav_90">OTIS ELEVATOR COMPANY (S) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_91" value="X77R29PHU641OQLO8U71">
              <label class="selection" for="employersFav_91">STRAITS CONSTRUCTION SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_92" value="K5XHIPYES1AZZ4B7X3U6">
              <label class="selection" for="employersFav_92">HOME TEAM SCIENCE AND TECHNOLOGY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_93" value="ZLCUGRHLBT00OCUAY8M0">
              <label class="selection" for="employersFav_93">G-ENERGY GLOBAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_94" value="RKJOFXM9JWZLG3IAHTI2">
              <label class="selection" for="employersFav_94">LITE-ON SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_95" value="65DRATQE9J7ABAIG3WZ9">
              <label class="selection" for="employersFav_95">MATCOR TECHNOLOGY &amp; SERVICES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_96" value="M7IBZ8XNTKND0AM5SNA4">
              <label class="selection" for="employersFav_96">TRINA SOLAR ENERGY DEVELOPMENT PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_97" value="A5C64QESKMHOQ3G9F996">
              <label class="selection" for="employersFav_97">BDO LLP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_98" value="9OH21YDQ0TG8IR8ZXEH9">
              <label class="selection" for="employersFav_98">PSA CORPORATION LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_99" value="T0T4X1XS5MH9LTP325L1">
              <label class="selection" for="employersFav_99">LIT STRATEGY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_100" value="2JWS03NM5KGXN4JCAQT3">
              <label class="selection" for="employersFav_100">PHILLIPCAPITAL</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_101" value="WIK4S2CM88P0270DKUQ8">
              <label class="selection" for="employersFav_101">HAPAG-LLOYD PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_102" value="UNJEMN1X34OKL6Y0FNF5">
              <label class="selection" for="employersFav_102">CLA GLOBAL TS HOLDINGS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_103" value="DGNKLSPGFONR01XQ8ZF8">
              <label class="selection" for="employersFav_103">APECUS TECHNOLOGIES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_104" value="ORW6PYK0QG85GEDB3GD4">
              <label class="selection" for="employersFav_104">GROUNDUP.AI PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_105" value="893G3O3XJ9XJRU1OBYY1">
              <label class="selection" for="employersFav_105">GLOBALFOUNDRIES SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_106" value="KSJ0JATNY5DAMRHJ7971">
              <label class="selection" for="employersFav_106">ANACLE SYSTEMS LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_107" value="TILLH8IMWABLOLF1EXW8">
              <label class="selection" for="employersFav_107">SUADE LABS </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_108" value="WCDKG1LCCYOYTY15SMC5">
              <label class="selection" for="employersFav_108">TEAMBUILD ENGINEERING &amp; CONSTRUCTION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_109" value="PKZO7YAR3PRA8L8H8SH2">
              <label class="selection" for="employersFav_109">ASE SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_110" value="9AMT1PCXQ0N1DQWOIUP7">
              <label class="selection" for="employersFav_110">SSG</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_111" value="DGZPE2639KQZ9BJ0ZE25">
              <label class="selection" for="employersFav_111">BERY MARITIME SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_112" value="Z52DSIYWFUL92H5YC498">
              <label class="selection" for="employersFav_112">WK ASIA-PACIFIC ENVIRONMENTAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_113" value="1JAUAYBW365RIFLCWYW0">
              <label class="selection" for="employersFav_113">SURBANA JURONG GROUP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_114" value="FTUGIX5LSIDR63G5S9U6">
              <label class="selection" for="employersFav_114">BACHY SOLETANCHE SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_115" value="4JBRXIZONC49W1R23G61">
              <label class="selection" for="employersFav_115">AMEC FOSTER WHEELER ASIA PACIFIC PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_116" value="K6LWH6IMWTPD71DPEZK2">
              <label class="selection" for="employersFav_116">MINISTRY OF MANPOWER (MOM)</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_117" value="3E3SZR4ES4YOPEUEII42">
              <label class="selection" for="employersFav_117">COSCO SHIPPING SPECIALIZED CARRIERS(SOUTHEAST ASIA) PTE.LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_118" value="6KU34XJCAKPY5BD995B0">
              <label class="selection" for="employersFav_118">SETSCO SERVICES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_119" value="DTZBRQTX00DDILL2RTF6">
              <label class="selection" for="employersFav_119">STMICROELECTRONICS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_120" value="NKZ5K4RFTM0O5F6TJ7Z5">
              <label class="selection" for="employersFav_120">THE LEARNINGLAB EDUCATION CENTRE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_121" value="B4ICUACBUI2DN4DBAT88">
              <label class="selection" for="employersFav_121">AFFINITY TANKERS PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_122" value="IKRWSNX46ZH06ZNKJNN9">
              <label class="selection" for="employersFav_122">EDUEDGE LEARNING HUB PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_123" value="2G3WPYBIETNLGUZ74M96">
              <label class="selection" for="employersFav_123">SHIMADZU (ASIA PACIFIC) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_124" value="FXF20N70JKJUE2D3IDS6">
              <label class="selection" for="employersFav_124">INSIGHT ASIA RESEARCH GROUP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_125" value="IG02Y6983P08286DWWI3">
              <label class="selection" for="employersFav_125">KGI SECURITIES (SINGAPORE) PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_126" value="78YDO9BJ0M5C6CG6DYH9">
              <label class="selection" for="employersFav_126">CRAFTSMAN TECH PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_127" value="K86WHMJR9UM0SBASTUD2">
              <label class="selection" for="employersFav_127">WSP CONSULTANCY PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_128" value="RZW759ST7L6FD39L90C7">
              <label class="selection" for="employersFav_128">NTT SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_129" value="NKL1YT5OTUM2ZUBJ0R71">
              <label class="selection" for="employersFav_129">KORDAMENTHA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_130" value="XUTJBJZZEBAT7MENR032">
              <label class="selection" for="employersFav_130">NETE2 ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_131" value="7ZM9BRDM8013NW38ZX19">
              <label class="selection" for="employersFav_131">AGENCY FOR SCIENCE, TECHNOLOGY AND RESEARCH</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_132" value="B7PRULNZAE01Y8RAXUR1">
              <label class="selection" for="employersFav_132">ED&amp;F MAN ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_133" value="BK6KDRZ8Y478J214N7I2">
              <label class="selection" for="employersFav_133">PURPLEFOREST EVENTS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_134" value="7SUI1UDWSNM5ZE8DETK9">
              <label class="selection" for="employersFav_134">DSO NATIONAL LABORATORIES</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_135" value="771BHMAIZUXIRUOFU223">
              <label class="selection" for="employersFav_135">ISO-TEAM CORPORATION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_136" value="0GZ2DWLGLIDINBPLZZC9">
              <label class="selection" for="employersFav_136">MINISTRY OF TRADE AND INDUSTRY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_137" value="4JXTS7L1DQW3DLXT7JO7">
              <label class="selection" for="employersFav_137">DHL SUPPLY CHAIN</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_138" value="SYDOLYH1AXGLB7MCDU89">
              <label class="selection" for="employersFav_138">WESTCON SOLUTIONS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_139" value="HIF80NULZ0CS0NIRLBH7">
              <label class="selection" for="employersFav_139">GRAND VENTURE TECHNOLOGY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_140" value="LRKJDP2ENXP9R3KRITQ9">
              <label class="selection" for="employersFav_140">STARFIVE INTERNATIONAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_141" value="990535S2DQDN0D0WEQK4">
              <label class="selection" for="employersFav_141">SAVINGS4U PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_142" value="GJ3I0ZMRWSBDGYXJYY05">
              <label class="selection" for="employersFav_142">ADVANCED MICRO DEVICES</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_143" value="PYEC31LIPT57AR3LLQH8">
              <label class="selection" for="employersFav_143">PEPPERL-FUCHS ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_144" value="Z1K3TUNB1ZLEKJBRK8W1">
              <label class="selection" for="employersFav_144">ROTARY ENGINEERING PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_145" value="JHBZ8Q2UA4UWSTZB9TX5">
              <label class="selection" for="employersFav_145">BIPO SERVICE PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_146" value="YGPKCTON4MBIXIT6PPC4">
              <label class="selection" for="employersFav_146">MEADWAY SHIPPING SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_147" value="TRELSDESG41F3M0LPM21">
              <label class="selection" for="employersFav_147">LIONSBOT INTERNATIONAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_148" value="8LFZZW2J17IBRD2CAFG9">
              <label class="selection" for="employersFav_148">BAHWAN CYBERTEK PTE LTD </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_149" value="41O37I9NF96XEZ8F9IT5">
              <label class="selection" for="employersFav_149">FDM SINGAPORE CONSULTING PTE. LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_150" value="RS1IH7B1EJG8KHJWZDU7">
              <label class="selection" for="employersFav_150">ONEBERRY TECHNOLOGIES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_151" value="AF6D2QG82X00M0TTW0A4">
              <label class="selection" for="employersFav_151">JARDINE ENGINEERING (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_152" value="WIN7FABBQZTUBCJKC4N8">
              <label class="selection" for="employersFav_152">SMITECH ENGINEERING PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_153" value="9T4QB143B9NYGNS0OLW1">
              <label class="selection" for="employersFav_153">VSL SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_154" value="JOY8MHZIQZJ76DHKZP10">
              <label class="selection" for="employersFav_154">NUCLEUS SOFTWARE SOLUTIONS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_155" value="XH3M9QR29CL5ZYZMQXL8">
              <label class="selection" for="employersFav_155">IMMIGRATION AND CHECKPOINTS AUTHORITY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_156" value="5IUCXOO7Q2FOO51SYB15">
              <label class="selection" for="employersFav_156">FORMWORK HIRE (S.E.A) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_157" value="S14FPWZKBZLRG1ZQKXZ2">
              <label class="selection" for="employersFav_157">KINGSMEN EXHIBITS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_158" value="JQJ11TUJJFPX98UWJN88">
              <label class="selection" for="employersFav_158">ACCELLION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_159" value="J61WM76WOFCT61AYUMX1">
              <label class="selection" for="employersFav_159">REPUBLIC OF SINGAPORE NAVY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_160" value="SLXBOBPF7UDIPT2RKRY2">
              <label class="selection" for="employersFav_160">THE PIQUE LAB PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_161" value="UEJM0DMTICFSUQR3IN64">
              <label class="selection" for="employersFav_161">BUILDERS 265 PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_162" value="ERG9AJRU8ATODHLQ8AE8">
              <label class="selection" for="employersFav_162">UNITED OVERSEAS BANK</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_163" value="G1TPRUZOIZBQNH5Z0YN9">
              <label class="selection" for="employersFav_163">WORLEY PTE LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_164" value="00GBWRR7H9D5XWHMT7P7">
              <label class="selection" for="employersFav_164">WHITE SPACE DIGITAL PTE LTD </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_165" value="U6SDCSRTUJRSZXYO6BT6">
              <label class="selection" for="employersFav_165">OMNIVISION TECHNOLOGIES S'PORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_166" value="1FWBJNXXJE7A2WJ9ZN37">
              <label class="selection" for="employersFav_166">DELIVEROO</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_167" value="GIHQTXRLPUXDLOKOGAR2">
              <label class="selection" for="employersFav_167">WAVELENGTH OPTO-ELECTRONIC (S) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_168" value="0AE9XA9I9PAC7IUB2BO1">
              <label class="selection" for="employersFav_168">SING INVESTMENTS &amp; FINANCE LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_169" value="Q1Y96DSHHFIASJQ63HZ1">
              <label class="selection" for="employersFav_169">GRANT THORNTON SINGAPORE PRIVATE LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_170" value="8MGMTI8JDGHLIGIAJ1L9">
              <label class="selection" for="employersFav_170">MAVERICK DERIVATIVES PTE. LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_171" value="O42KFMI4BCB439GXBQ86">
              <label class="selection" for="employersFav_171">SAUTER SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_172" value="7SFK88IB586CX04BA3T9">
              <label class="selection" for="employersFav_172">FLIGHT EXPERIENCE SINGAPORE PTE LTD </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_173" value="T5FSH7G8GAXJZ125L7X2">
              <label class="selection" for="employersFav_173">MATHVISION ENRICHMENT CENTRE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_174" value="GCRCRBPT3BTMHF2NMB86">
              <label class="selection" for="employersFav_174">HUAWEI INTERNATIONAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_175" value="PEBRNXRQMABC32WOI385">
              <label class="selection" for="employersFav_175">NANYANG TECHNOLOGICAL UNIVERSITY</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_176" value="464Z4QK5PNHHHD59TUC2">
              <label class="selection" for="employersFav_176">LUXOFT INFORMATION TECHNOLOGY (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_177" value="RMIGH9GB6FANFU7A7YM2">
              <label class="selection" for="employersFav_177">ROLLING ARRAYS CONSULTING PTE.LTD.</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_178" value="NZBYRK0IWI8J7821LUK6">
              <label class="selection" for="employersFav_178">IB SUPER</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_179" value="P46HX6HHX7NFAICWW269">
              <label class="selection" for="employersFav_179">BUSINESS CONTINUITY PLANNING ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_180" value="EWCO6BEMMSTPI0SCC6P8">
              <label class="selection" for="employersFav_180">CENTRAL PROVIDENT FUND BOARD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_181" value="2RSYR720L48UQ4JSMBK1">
              <label class="selection" for="employersFav_181">DXC TECHNOLOGY SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_182" value="LFXRDIDE1M77YE6T6D76">
              <label class="selection" for="employersFav_182">AMERICAN EXPRESS SINGAPORE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_183" value="9ZC78ULC2ASLSTIX4PA1">
              <label class="selection" for="employersFav_183">CHICHIBU CONSULTING</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_184" value="Z7HDEE0NXBMETWDUAW51">
              <label class="selection" for="employersFav_184">MINISTRY OF FOREIGN AFFAIRS</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_185" value="PO721QI82W6DDNZ0Q6J4">
              <label class="selection" for="employersFav_185">MAHA CHEMICALS (ASIA) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_186" value="OWODQ5DF5UQZGI5XZ222">
              <label class="selection" for="employersFav_186">TRICOR SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_187" value="APPDZDBYAX1AQP23L153">
              <label class="selection" for="employersFav_187">PCS SECURITY PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_188" value="O4GIKP9761L749SZZQR0">
              <label class="selection" for="employersFav_188">SURECOMP ASIA PACIFIC PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_189" value="FLS90BMIYBXRCX3UNMO3">
              <label class="selection" for="employersFav_189">MIND STRETCHER EDUCATION PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_190" value="F6S22WDWGO1SUCGI12U3">
              <label class="selection" for="employersFav_190">WINMARK INVESTMENTS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_191" value="5H9FS7XJPHOU8DU802S1">
              <label class="selection" for="employersFav_191">HOYOVERSE</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_192" value="AHPJWZXSN1XAHEMJYJZ8">
              <label class="selection" for="employersFav_192">IN.CORP GLOBAL PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_193" value="MHWDTNB2QHHJ53EMYMK1">
              <label class="selection" for="employersFav_193">JONES LANG LASALLE PROPERTY CONSULTANTS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_194" value="J8FZDTUMQ8N9L9LEEWL1">
              <label class="selection" for="employersFav_194">SAFRAN LANDING SYSTEMS SINGAPORE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_195" value="6YL1QAUD5DLAU6NB29G3">
              <label class="selection" for="employersFav_195">DFI RETAIL GROUP</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_196" value="DMIQZZ0SR9M57KW31BO4">
              <label class="selection" for="employersFav_196">KLA-TENCOR (SINGAPORE) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_197" value="SXLUOC2NK7NAZS1H71P8">
              <label class="selection" for="employersFav_197">MAYBANK SINGAPORE LIMITED</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_198" value="2WQ38XO8KXI2IGT467A0">
              <label class="selection" for="employersFav_198">SINGAPORE HEALTH SERVICES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_199" value="TNX590NLSRWSQ08KBYH0">
              <label class="selection" for="employersFav_199">L&amp;T TECHNOLOGY SERVICES</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_200" value="9E38XHJTCYF61H3MRMD2">
              <label class="selection" for="employersFav_200">HATCH TECHNOLOGIES PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_201" value="BRU188DUB3ZPPMGU0JW9">
              <label class="selection" for="employersFav_201">Q SQUARED SOLUTIONS</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_202" value="LCKFT1UKAFL3Z1YMK035">
              <label class="selection" for="employersFav_202">KELLER FOUNDATIONS (SE ASIA) PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_203" value="RU395LZ11ATRL28D4EJ6">
              <label class="selection" for="employersFav_203">G &amp; W READY-MIX PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_204" value="JLKZJFNTX942W81O5NC1">
              <label class="selection" for="employersFav_204">TAURUS ONE PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_205" value="8UONMFJ5R97B0OOCR8H3">
              <label class="selection" for="employersFav_205">BULOX POWER PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_206" value="W964L853TRT3EUPGYER4">
              <label class="selection" for="employersFav_206">LONZA BIOLOGICS TUAS PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_207" value="EADIS1JGGNE8FL9UEJ43">
              <label class="selection" for="employersFav_207">DIAGNOSTICS DEVELOPMENT HUB, ASTAR </label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_208" value="N1D9DSLMN1YMD09X3FS9">
              <label class="selection" for="employersFav_208">SAP ASIA PTE LTD</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_209" value="F3GUOEYA1N52M8HKJJP9">
              <label class="selection" for="employersFav_209">JTC CORPORATION</label>
            </div>
                        <div>
              <input type="checkbox" name="employersFav[]" id="employersFav_210" value="XPPMM7WSKHEF7PB2IU41">
              <label class="selection" for="employersFav_210">ROHDE &amp; SCHWARZ ASIA PTE LTD</label>
            </div>
                      </div>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
divs = soup.find_all('div', {'class': 'empList'})

labels_array = []
for div in divs:
    labels_array.append(re.findall(r'<label.*?>(.*?)</label>', str(div)))


for labels in labels_array:
    with open('labels.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Label'])
        for label in labels:
            print(label)
            writer.writerow([label])
