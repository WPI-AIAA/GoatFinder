<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="8.4.1">
<drawing>
<settings>
<setting alwaysvectorfont="yes"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="24" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="GoatFinder">
<packages>
<package name="GPS">
<smd name="P$1" x="-7.62" y="2.54" dx="2" dy="1" layer="1"/>
<smd name="P$2" x="-7.62" y="1.04" dx="2" dy="1" layer="1"/>
<smd name="P$3" x="-7.62" y="-0.46" dx="2" dy="1" layer="1"/>
<smd name="P$4" x="-7.62" y="-1.96" dx="2" dy="1" layer="1"/>
<smd name="P$5" x="-7.62" y="-3.46" dx="2" dy="1" layer="1"/>
<smd name="P$6" x="-7.62" y="-4.96" dx="2" dy="1" layer="1"/>
<smd name="P$7" x="-7.62" y="-6.46" dx="2" dy="1" layer="1"/>
<smd name="P$8" x="-7.62" y="-7.96" dx="2" dy="1" layer="1"/>
<smd name="P$9" x="-7.62" y="-9.46" dx="2" dy="1" layer="1"/>
<smd name="P$10" x="-7.62" y="-10.96" dx="2" dy="1" layer="1"/>
<smd name="P$11" x="8.38" y="-10.96" dx="2" dy="1" layer="1"/>
<smd name="P$12" x="8.38" y="-9.46" dx="2" dy="1" layer="1"/>
<smd name="P$13" x="8.38" y="-7.96" dx="2" dy="1" layer="1"/>
<smd name="P$14" x="8.38" y="-6.46" dx="2" dy="1" layer="1"/>
<smd name="P$15" x="8.38" y="-4.96" dx="2" dy="1" layer="1"/>
<smd name="P$16" x="8.38" y="-3.46" dx="2" dy="1" layer="1"/>
<smd name="P$17" x="8.38" y="-1.96" dx="2" dy="1" layer="1"/>
<smd name="P$18" x="8.38" y="-0.46" dx="2" dy="1" layer="1"/>
<smd name="P$19" x="8.38" y="1.04" dx="2" dy="1" layer="1"/>
<smd name="P$20" x="8.38" y="2.54" dx="2" dy="1" layer="1"/>
<wire x1="-6.12" y1="3.04" x2="-6.12" y2="-11.46" width="0.127" layer="21"/>
<wire x1="-6.12" y1="-11.46" x2="6.88" y2="-11.46" width="0.127" layer="21"/>
<wire x1="6.88" y1="-11.46" x2="6.88" y2="3.04" width="0.127" layer="21"/>
<wire x1="6.88" y1="3.04" x2="-6.12" y2="3.04" width="0.127" layer="21"/>
<circle x="-5.12" y="2.04" radius="0.5" width="0.127" layer="21"/>
<text x="0.38" y="-3.46" size="2.54" layer="21" font="vector" align="center">GPS</text>
</package>
<package name="9DOF">
<wire x1="16.51" y1="5.842" x2="16.51" y2="-9.398" width="0.127" layer="21"/>
<wire x1="-16.51" y1="-9.398" x2="-16.51" y2="5.842" width="0.127" layer="21"/>
<wire x1="-13.97" y1="8.382" x2="13.97" y2="8.382" width="0.127" layer="21"/>
<wire x1="-13.97" y1="-11.938" x2="13.97" y2="-11.938" width="0.127" layer="21"/>
<wire x1="-16.51" y1="5.842" x2="-13.97" y2="8.382" width="0.127" layer="21" curve="-90"/>
<wire x1="-13.97" y1="-11.938" x2="-16.51" y2="-9.398" width="0.127" layer="21" curve="-90"/>
<wire x1="16.51" y1="-9.398" x2="13.97" y2="-11.938" width="0.127" layer="21" curve="-90"/>
<wire x1="13.97" y1="8.382" x2="16.51" y2="5.842" width="0.127" layer="21" curve="-90"/>
<circle x="0" y="0" radius="1.27" width="0.127" layer="21"/>
<smd name="P$15" x="-5.08" y="7.557" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$16" x="-2.54" y="4.127" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$17" x="0" y="7.557" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$18" x="2.54" y="4.127" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$19" x="5.08" y="7.557" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$20" x="-10.16" y="-7.683" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$21" x="-7.62" y="-11.113" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$22" x="-5.08" y="-7.683" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$23" x="-2.54" y="-11.113" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$24" x="0" y="-7.683" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$25" x="2.54" y="-11.113" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$26" x="5.08" y="-7.683" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$27" x="7.62" y="-11.113" dx="2.03" dy="1.27" layer="1" rot="R90"/>
<smd name="P$28" x="10.16" y="-7.683" dx="2.03" dy="1.27" layer="1" rot="R90"/>
</package>
<package name="USB_VERTICLE">
<pad name="VCC" x="3.5" y="0" drill="0.92" shape="square"/>
<pad name="D-" x="1" y="0" drill="0.92"/>
<pad name="D+" x="-1" y="0" drill="0.92"/>
<pad name="GND@1" x="-3.5" y="0" drill="0.92" rot="R180"/>
<wire x1="-6.4" y1="2.2" x2="-6.4" y2="0.8" width="0.6" layer="46"/>
<wire x1="6.4" y1="0.8" x2="6.4" y2="2.2" width="0.6" layer="46"/>
<wire x1="-6.4" y1="2.5" x2="-6.4" y2="0.5" width="1.2" layer="17"/>
<wire x1="6.4" y1="2.5" x2="6.4" y2="0.5" width="1.2" layer="17"/>
<pad name="GND@2" x="-6.4" y="1.5" drill="0.6" shape="long" rot="R270"/>
<pad name="GND@3" x="6.4" y="1.5" drill="0.6" shape="long" rot="R270"/>
</package>
<package name="PI_HEADER_SMD">
<smd name="3.3V@1" x="-24.13" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="5V@2" x="-24.13" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="SDA1" x="-21.59" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="5V@4" x="-21.59" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="SCL1" x="-19.05" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@6" x="-19.05" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO7" x="-16.51" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="TXD" x="-16.51" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@9" x="-13.97" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="RXD" x="-13.97" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO0" x="-11.43" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO1" x="-11.43" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO2" x="-8.89" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@14" x="-8.89" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO3" x="-6.35" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO4" x="-6.35" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="3.3V@17" x="-3.81" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO5" x="-3.81" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="MOSI" x="-1.27" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@20" x="-1.27" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="MISO" x="1.27" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO6" x="1.27" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="SCLK" x="3.81" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="CE0" x="3.81" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@25" x="6.35" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="CE1" x="6.35" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="SDA0" x="8.89" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="SCL0" x="8.89" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO21" x="11.43" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@30" x="11.43" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO22" x="13.97" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO26" x="13.97" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO23" x="16.51" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@34" x="16.51" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO24" x="19.05" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO27" x="19.05" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO25" x="21.59" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO28" x="21.59" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GND@39" x="24.13" y="2.54" dx="3.175" dy="1.27" layer="16" rot="R90"/>
<smd name="GPIO29" x="24.13" y="-2.921" dx="3.175" dy="1.27" layer="16" rot="R90"/>
</package>
<package name="ETHERNET">
<wire x1="0" y1="0" x2="0" y2="-15.494" width="0.127" layer="21"/>
<wire x1="0" y1="-15.494" x2="16.002" y2="-15.494" width="0.127" layer="21"/>
<wire x1="16.002" y1="-15.494" x2="16.002" y2="0" width="0.127" layer="21"/>
<wire x1="16.002" y1="0" x2="0" y2="0" width="0.127" layer="21"/>
<wire x1="2.54" y1="-1.27" x2="11.43" y2="-1.27" width="0.127" layer="21"/>
<wire x1="11.43" y1="-1.27" x2="11.43" y2="-5.08" width="0.127" layer="21"/>
<wire x1="11.43" y1="-5.08" x2="13.97" y2="-5.08" width="0.127" layer="21"/>
<wire x1="13.97" y1="-5.08" x2="13.97" y2="-10.16" width="0.127" layer="21"/>
<wire x1="13.97" y1="-10.16" x2="11.43" y2="-10.16" width="0.127" layer="21"/>
<wire x1="11.43" y1="-10.16" x2="11.43" y2="-13.97" width="0.127" layer="21"/>
<wire x1="11.43" y1="-13.97" x2="2.54" y2="-13.97" width="0.127" layer="21"/>
<wire x1="2.54" y1="-13.97" x2="2.54" y2="-1.27" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="GPS">
<pin name="VCC" x="-15.24" y="2.54" visible="pin" length="short"/>
<pin name="RESET" x="-15.24" y="0" visible="pin" length="short"/>
<pin name="GND@1" x="-15.24" y="-2.54" visible="pin" length="short"/>
<pin name="BACK" x="-15.24" y="-5.08" visible="pin" length="short"/>
<pin name="3D" x="-15.24" y="-7.62" visible="pin" length="short"/>
<pin name="NC@1" x="-15.24" y="-10.16" visible="pin" length="short"/>
<pin name="NC@2" x="-15.24" y="-12.7" visible="pin" length="short"/>
<pin name="GND@2" x="-15.24" y="-15.24" visible="pin" length="short"/>
<pin name="TX" x="-15.24" y="-17.78" visible="pin" length="short"/>
<pin name="RX" x="-15.24" y="-20.32" visible="pin" length="short"/>
<pin name="ANT" x="15.24" y="-20.32" visible="pin" length="short" rot="R180"/>
<pin name="GND@3" x="15.24" y="-17.78" visible="pin" length="short" rot="R180"/>
<pin name="1PPS" x="15.24" y="-15.24" visible="pin" length="short" rot="R180"/>
<pin name="RTCM" x="15.24" y="-12.7" visible="pin" length="short" rot="R180"/>
<pin name="NC@3" x="15.24" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="NC@4" x="15.24" y="-7.62" visible="pin" length="short" rot="R180"/>
<pin name="NC@5" x="15.24" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="NC@6" x="15.24" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="GND@4" x="15.24" y="0" visible="pin" length="short" rot="R180"/>
<pin name="NC@7" x="15.24" y="2.54" visible="pin" length="short" rot="R180"/>
<wire x1="-12.7" y1="5.08" x2="-12.7" y2="-22.86" width="0.254" layer="94"/>
<wire x1="-12.7" y1="-22.86" x2="12.7" y2="-22.86" width="0.254" layer="94"/>
<wire x1="12.7" y1="-22.86" x2="12.7" y2="5.08" width="0.254" layer="94"/>
<wire x1="12.7" y1="5.08" x2="-12.7" y2="5.08" width="0.254" layer="94"/>
<text x="0" y="-2.54" size="2.54" layer="94" font="vector" rot="R180" align="center">GPS</text>
</symbol>
<symbol name="9DOF">
<pin name="DEN" x="-10.16" y="-5.08" visible="pin" length="short"/>
<pin name="INT2" x="-10.16" y="-2.54" visible="pin" length="short"/>
<pin name="INT1" x="-10.16" y="0" visible="pin" length="short"/>
<pin name="DRDY" x="-10.16" y="2.54" visible="pin" length="short"/>
<pin name="INTG" x="-10.16" y="5.08" visible="pin" length="short"/>
<pin name="VIN" x="10.16" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="3V3" x="10.16" y="-7.62" visible="pin" length="short" rot="R180"/>
<pin name="GND" x="10.16" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="SCL" x="10.16" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="SDA" x="10.16" y="0" visible="pin" length="short" rot="R180"/>
<pin name="CSG" x="10.16" y="2.54" visible="pin" length="short" rot="R180"/>
<pin name="CSXM" x="10.16" y="5.08" visible="pin" length="short" rot="R180"/>
<pin name="SDOG" x="10.16" y="7.62" visible="pin" length="short" rot="R180"/>
<pin name="?" x="10.16" y="10.16" visible="pin" length="short" rot="R180"/>
<wire x1="-7.62" y1="-12.7" x2="-7.62" y2="12.7" width="0.254" layer="94"/>
<wire x1="-7.62" y1="12.7" x2="7.62" y2="12.7" width="0.254" layer="94"/>
<wire x1="7.62" y1="12.7" x2="7.62" y2="-12.7" width="0.254" layer="94"/>
<wire x1="7.62" y1="-12.7" x2="-7.62" y2="-12.7" width="0.254" layer="94"/>
<text x="-2.54" y="-10.16" size="2.54" layer="94" align="center">9DOF</text>
</symbol>
<symbol name="USB">
<wire x1="5.08" y1="2.54" x2="5.08" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="5.08" y1="-10.16" x2="-5.08" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="-10.16" x2="-5.08" y2="2.54" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="2.54" x2="5.08" y2="2.54" width="0.1524" layer="94"/>
<pin name="+5V" x="7.62" y="0" visible="pin" length="short" rot="R180"/>
<pin name="D-" x="7.62" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="D+" x="7.62" y="-5.08" visible="pin" length="short" rot="R180"/>
<pin name="GND" x="7.62" y="-7.62" visible="pin" length="short" rot="R180"/>
</symbol>
<symbol name="PI">
<wire x1="-2.54" y1="2.54" x2="20.32" y2="2.54" width="0.254" layer="94"/>
<pin name="5V@2" x="-5.08" y="0" visible="pin" length="short"/>
<pin name="5V@4" x="-5.08" y="-2.54" visible="pin" length="short"/>
<pin name="3.3V@1" x="-5.08" y="-7.62" visible="pin" length="short"/>
<pin name="3.3V@2" x="-5.08" y="-10.16" visible="pin" length="short"/>
<pin name="GND@1" x="-5.08" y="-15.24" visible="pin" length="short"/>
<pin name="GND@2" x="-5.08" y="-17.78" visible="pin" length="short"/>
<pin name="GND@3" x="-5.08" y="-20.32" visible="pin" length="short"/>
<pin name="GND@4" x="-5.08" y="-22.86" visible="pin" length="short"/>
<pin name="GND@5" x="-5.08" y="-27.94" visible="pin" length="short"/>
<pin name="GND@6" x="-5.08" y="-30.48" visible="pin" length="short"/>
<pin name="GND@7" x="-5.08" y="-33.02" visible="pin" length="short"/>
<pin name="GND@8" x="-5.08" y="-35.56" visible="pin" length="short"/>
<pin name="SDA0" x="22.86" y="0" visible="pin" length="short" rot="R180"/>
<pin name="SCL0" x="22.86" y="-2.54" visible="pin" length="short" rot="R180"/>
<pin name="SDA1" x="22.86" y="-7.62" visible="pin" length="short" rot="R180"/>
<pin name="SCL1" x="22.86" y="-10.16" visible="pin" length="short" rot="R180"/>
<pin name="MOSI" x="22.86" y="-15.24" visible="pin" length="short" rot="R180"/>
<pin name="SCLK" x="22.86" y="-20.32" visible="pin" length="short" rot="R180"/>
<pin name="MISO" x="22.86" y="-17.78" visible="pin" length="short" rot="R180"/>
<pin name="CE0" x="22.86" y="-25.4" visible="pin" length="short" rot="R180"/>
<pin name="CE1" x="22.86" y="-27.94" visible="pin" length="short" rot="R180"/>
<pin name="TXD" x="22.86" y="-33.02" visible="pin" length="short" rot="R180"/>
<pin name="RXD" x="22.86" y="-35.56" visible="pin" length="short" rot="R180"/>
<wire x1="20.32" y1="2.54" x2="20.32" y2="-63.5" width="0.254" layer="94"/>
<wire x1="20.32" y1="-63.5" x2="-2.54" y2="-63.5" width="0.254" layer="94"/>
<wire x1="-2.54" y1="-63.5" x2="-2.54" y2="2.54" width="0.254" layer="94"/>
<pin name="GPIO0" x="-5.08" y="-40.64" visible="pin" length="short"/>
<pin name="GPIO1" x="-5.08" y="-43.18" visible="pin" length="short"/>
<pin name="GPIO2" x="-5.08" y="-45.72" visible="pin" length="short"/>
<pin name="GPIO3" x="-5.08" y="-48.26" visible="pin" length="short"/>
<pin name="GPIO4" x="-5.08" y="-50.8" visible="pin" length="short"/>
<pin name="GPIO5" x="-5.08" y="-53.34" visible="pin" length="short"/>
<pin name="GPIO6" x="-5.08" y="-55.88" visible="pin" length="short"/>
<pin name="GPIO7" x="-5.08" y="-58.42" visible="pin" length="short"/>
<pin name="GPIO29" x="22.86" y="-60.96" visible="pin" length="short" rot="R180"/>
<pin name="GPIO21" x="22.86" y="-40.64" visible="pin" length="short" rot="R180"/>
<pin name="GPIO22" x="22.86" y="-43.18" visible="pin" length="short" rot="R180"/>
<pin name="GPIO23" x="22.86" y="-45.72" visible="pin" length="short" rot="R180"/>
<pin name="GPIO24" x="22.86" y="-48.26" visible="pin" length="short" rot="R180"/>
<pin name="GPIO25" x="22.86" y="-50.8" visible="pin" length="short" rot="R180"/>
<pin name="GPIO26" x="22.86" y="-53.34" visible="pin" length="short" rot="R180"/>
<pin name="GPIO27" x="22.86" y="-55.88" visible="pin" length="short" rot="R180"/>
<pin name="GPIO28" x="22.86" y="-58.42" visible="pin" length="short" rot="R180"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="GPS">
<gates>
<gate name="G$1" symbol="GPS" x="0" y="2.54"/>
</gates>
<devices>
<device name="" package="GPS">
<connects>
<connect gate="G$1" pin="1PPS" pad="P$13"/>
<connect gate="G$1" pin="3D" pad="P$5"/>
<connect gate="G$1" pin="ANT" pad="P$11"/>
<connect gate="G$1" pin="BACK" pad="P$4"/>
<connect gate="G$1" pin="GND@1" pad="P$3"/>
<connect gate="G$1" pin="GND@2" pad="P$8"/>
<connect gate="G$1" pin="GND@3" pad="P$12"/>
<connect gate="G$1" pin="GND@4" pad="P$19"/>
<connect gate="G$1" pin="NC@1" pad="P$6"/>
<connect gate="G$1" pin="NC@2" pad="P$7"/>
<connect gate="G$1" pin="NC@3" pad="P$15"/>
<connect gate="G$1" pin="NC@4" pad="P$16"/>
<connect gate="G$1" pin="NC@5" pad="P$17"/>
<connect gate="G$1" pin="NC@6" pad="P$18"/>
<connect gate="G$1" pin="NC@7" pad="P$20"/>
<connect gate="G$1" pin="RESET" pad="P$2"/>
<connect gate="G$1" pin="RTCM" pad="P$14"/>
<connect gate="G$1" pin="RX" pad="P$10"/>
<connect gate="G$1" pin="TX" pad="P$9"/>
<connect gate="G$1" pin="VCC" pad="P$1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="9DOF">
<gates>
<gate name="G$1" symbol="9DOF" x="0" y="0"/>
</gates>
<devices>
<device name="" package="9DOF">
<connects>
<connect gate="G$1" pin="3V3" pad="P$21"/>
<connect gate="G$1" pin="?" pad="P$28"/>
<connect gate="G$1" pin="CSG" pad="P$25"/>
<connect gate="G$1" pin="CSXM" pad="P$26"/>
<connect gate="G$1" pin="DEN" pad="P$15"/>
<connect gate="G$1" pin="DRDY" pad="P$18" route="any"/>
<connect gate="G$1" pin="GND" pad="P$22"/>
<connect gate="G$1" pin="INT1" pad="P$17" route="any"/>
<connect gate="G$1" pin="INT2" pad="P$16"/>
<connect gate="G$1" pin="INTG" pad="P$19"/>
<connect gate="G$1" pin="SCL" pad="P$23"/>
<connect gate="G$1" pin="SDA" pad="P$24"/>
<connect gate="G$1" pin="SDOG" pad="P$27"/>
<connect gate="G$1" pin="VIN" pad="P$20"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="USB_VERTICLE">
<gates>
<gate name="G$1" symbol="USB" x="2.54" y="0"/>
</gates>
<devices>
<device name="" package="USB_VERTICLE">
<connects>
<connect gate="G$1" pin="+5V" pad="VCC"/>
<connect gate="G$1" pin="D+" pad="D+"/>
<connect gate="G$1" pin="D-" pad="D-"/>
<connect gate="G$1" pin="GND" pad="GND@1 GND@2 GND@3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PI">
<gates>
<gate name="G$1" symbol="PI" x="-10.16" y="30.48"/>
</gates>
<devices>
<device name="" package="PI_HEADER_SMD">
<connects>
<connect gate="G$1" pin="3.3V@1" pad="3.3V@1"/>
<connect gate="G$1" pin="3.3V@2" pad="3.3V@17"/>
<connect gate="G$1" pin="5V@2" pad="5V@2"/>
<connect gate="G$1" pin="5V@4" pad="5V@4"/>
<connect gate="G$1" pin="CE0" pad="CE0"/>
<connect gate="G$1" pin="CE1" pad="CE1"/>
<connect gate="G$1" pin="GND@1" pad="GND@6"/>
<connect gate="G$1" pin="GND@2" pad="GND@9"/>
<connect gate="G$1" pin="GND@3" pad="GND@14"/>
<connect gate="G$1" pin="GND@4" pad="GND@20"/>
<connect gate="G$1" pin="GND@5" pad="GND@25"/>
<connect gate="G$1" pin="GND@6" pad="GND@30"/>
<connect gate="G$1" pin="GND@7" pad="GND@34"/>
<connect gate="G$1" pin="GND@8" pad="GND@39"/>
<connect gate="G$1" pin="GPIO0" pad="GPIO0"/>
<connect gate="G$1" pin="GPIO1" pad="GPIO1"/>
<connect gate="G$1" pin="GPIO2" pad="GPIO2"/>
<connect gate="G$1" pin="GPIO21" pad="GPIO21"/>
<connect gate="G$1" pin="GPIO22" pad="GPIO22"/>
<connect gate="G$1" pin="GPIO23" pad="GPIO23"/>
<connect gate="G$1" pin="GPIO24" pad="GPIO24"/>
<connect gate="G$1" pin="GPIO25" pad="GPIO25"/>
<connect gate="G$1" pin="GPIO26" pad="GPIO26"/>
<connect gate="G$1" pin="GPIO27" pad="GPIO27"/>
<connect gate="G$1" pin="GPIO28" pad="GPIO28"/>
<connect gate="G$1" pin="GPIO29" pad="GPIO29"/>
<connect gate="G$1" pin="GPIO3" pad="GPIO3"/>
<connect gate="G$1" pin="GPIO4" pad="GPIO4"/>
<connect gate="G$1" pin="GPIO5" pad="GPIO5"/>
<connect gate="G$1" pin="GPIO6" pad="GPIO6"/>
<connect gate="G$1" pin="GPIO7" pad="GPIO7"/>
<connect gate="G$1" pin="MISO" pad="MISO"/>
<connect gate="G$1" pin="MOSI" pad="MOSI"/>
<connect gate="G$1" pin="RXD" pad="RXD"/>
<connect gate="G$1" pin="SCL0" pad="SCL0"/>
<connect gate="G$1" pin="SCL1" pad="SCL1"/>
<connect gate="G$1" pin="SCLK" pad="SCLK"/>
<connect gate="G$1" pin="SDA0" pad="SDA0"/>
<connect gate="G$1" pin="SDA1" pad="SDA1"/>
<connect gate="G$1" pin="TXD" pad="TXD"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="ETHERNET">
<gates>
</gates>
<devices>
<device name="" package="ETHERNET">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$5" library="GoatFinder" deviceset="GPS" device=""/>
<part name="U$6" library="GoatFinder" deviceset="9DOF" device=""/>
<part name="U$8" library="GoatFinder" deviceset="USB_VERTICLE" device=""/>
<part name="U$11" library="GoatFinder" deviceset="PI" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$5" gate="G$1" x="139.7" y="78.74"/>
<instance part="U$6" gate="G$1" x="134.62" y="111.76"/>
<instance part="U$8" gate="G$1" x="38.1" y="142.24"/>
<instance part="U$11" gate="G$1" x="53.34" y="119.38"/>
</instances>
<busses>
</busses>
<nets>
<net name="+5V" class="0">
<segment>
<pinref part="U$6" gate="G$1" pin="VIN"/>
<wire x1="144.78" y1="101.6" x2="152.4" y2="101.6" width="0.1524" layer="91"/>
<label x="147.32" y="101.6" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$8" gate="G$1" pin="+5V"/>
<wire x1="45.72" y1="142.24" x2="55.88" y2="142.24" width="0.1524" layer="91"/>
<label x="50.8" y="142.24" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$11" gate="G$1" pin="5V@2"/>
<wire x1="48.26" y1="119.38" x2="45.72" y2="119.38" width="0.1524" layer="91"/>
<wire x1="45.72" y1="119.38" x2="45.72" y2="116.84" width="0.1524" layer="91"/>
<pinref part="U$11" gate="G$1" pin="5V@4"/>
<wire x1="45.72" y1="116.84" x2="48.26" y2="116.84" width="0.1524" layer="91"/>
<wire x1="45.72" y1="116.84" x2="35.56" y2="116.84" width="0.1524" layer="91"/>
<junction x="45.72" y="116.84"/>
<label x="35.56" y="116.84" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="U$5" gate="G$1" pin="GND@1"/>
<wire x1="124.46" y1="76.2" x2="116.84" y2="76.2" width="0.1524" layer="91"/>
<label x="116.84" y="76.2" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$5" gate="G$1" pin="GND@2"/>
<wire x1="124.46" y1="63.5" x2="116.84" y2="63.5" width="0.1524" layer="91"/>
<label x="116.84" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$5" gate="G$1" pin="GND@3"/>
<wire x1="154.94" y1="60.96" x2="162.56" y2="60.96" width="0.1524" layer="91"/>
<label x="157.48" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$5" gate="G$1" pin="GND@4"/>
<wire x1="154.94" y1="78.74" x2="162.56" y2="78.74" width="0.1524" layer="91"/>
<label x="157.48" y="78.74" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="GND"/>
<wire x1="144.78" y1="106.68" x2="152.4" y2="106.68" width="0.1524" layer="91"/>
<label x="147.32" y="106.68" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$8" gate="G$1" pin="GND"/>
<wire x1="45.72" y1="134.62" x2="55.88" y2="134.62" width="0.1524" layer="91"/>
<label x="50.8" y="134.62" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$11" gate="G$1" pin="GND@1"/>
<wire x1="48.26" y1="104.14" x2="45.72" y2="104.14" width="0.1524" layer="91"/>
<wire x1="45.72" y1="104.14" x2="45.72" y2="101.6" width="0.1524" layer="91"/>
<pinref part="U$11" gate="G$1" pin="GND@2"/>
<wire x1="45.72" y1="101.6" x2="48.26" y2="101.6" width="0.1524" layer="91"/>
<wire x1="45.72" y1="101.6" x2="45.72" y2="99.06" width="0.1524" layer="91"/>
<junction x="45.72" y="101.6"/>
<pinref part="U$11" gate="G$1" pin="GND@3"/>
<wire x1="45.72" y1="99.06" x2="48.26" y2="99.06" width="0.1524" layer="91"/>
<wire x1="45.72" y1="99.06" x2="45.72" y2="96.52" width="0.1524" layer="91"/>
<junction x="45.72" y="99.06"/>
<pinref part="U$11" gate="G$1" pin="GND@4"/>
<wire x1="45.72" y1="96.52" x2="48.26" y2="96.52" width="0.1524" layer="91"/>
<wire x1="45.72" y1="96.52" x2="35.56" y2="96.52" width="0.1524" layer="91"/>
<junction x="45.72" y="96.52"/>
<label x="35.56" y="96.52" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$11" gate="G$1" pin="GND@5"/>
<wire x1="48.26" y1="91.44" x2="45.72" y2="91.44" width="0.1524" layer="91"/>
<wire x1="45.72" y1="91.44" x2="45.72" y2="88.9" width="0.1524" layer="91"/>
<pinref part="U$11" gate="G$1" pin="GND@6"/>
<wire x1="45.72" y1="88.9" x2="48.26" y2="88.9" width="0.1524" layer="91"/>
<wire x1="45.72" y1="88.9" x2="45.72" y2="86.36" width="0.1524" layer="91"/>
<junction x="45.72" y="88.9"/>
<pinref part="U$11" gate="G$1" pin="GND@7"/>
<wire x1="45.72" y1="86.36" x2="48.26" y2="86.36" width="0.1524" layer="91"/>
<pinref part="U$11" gate="G$1" pin="GND@8"/>
<wire x1="45.72" y1="86.36" x2="45.72" y2="83.82" width="0.1524" layer="91"/>
<wire x1="45.72" y1="83.82" x2="48.26" y2="83.82" width="0.1524" layer="91"/>
<junction x="45.72" y="86.36"/>
<wire x1="45.72" y1="83.82" x2="35.56" y2="83.82" width="0.1524" layer="91"/>
<junction x="45.72" y="83.82"/>
<label x="35.56" y="83.82" size="1.778" layer="95"/>
</segment>
</net>
<net name="+3.3V" class="0">
<segment>
<pinref part="U$5" gate="G$1" pin="VCC"/>
<wire x1="124.46" y1="81.28" x2="116.84" y2="81.28" width="0.1524" layer="91"/>
<label x="116.84" y="81.28" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="3V3"/>
<wire x1="144.78" y1="104.14" x2="152.4" y2="104.14" width="0.1524" layer="91"/>
<label x="147.32" y="104.14" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$11" gate="G$1" pin="3.3V@1"/>
<wire x1="48.26" y1="111.76" x2="45.72" y2="111.76" width="0.1524" layer="91"/>
<wire x1="45.72" y1="111.76" x2="45.72" y2="109.22" width="0.1524" layer="91"/>
<pinref part="U$11" gate="G$1" pin="3.3V@2"/>
<wire x1="45.72" y1="109.22" x2="48.26" y2="109.22" width="0.1524" layer="91"/>
<wire x1="45.72" y1="109.22" x2="35.56" y2="109.22" width="0.1524" layer="91"/>
<junction x="45.72" y="109.22"/>
<label x="35.56" y="109.22" size="1.778" layer="95"/>
</segment>
</net>
<net name="CE0" class="0">
<segment>
<pinref part="U$11" gate="G$1" pin="CE0"/>
<wire x1="76.2" y1="93.98" x2="86.36" y2="93.98" width="0.1524" layer="91"/>
<label x="78.74" y="93.98" size="1.778" layer="95"/>
</segment>
</net>
<net name="SCL1" class="0">
<segment>
<pinref part="U$11" gate="G$1" pin="SCL1"/>
<wire x1="76.2" y1="109.22" x2="86.36" y2="109.22" width="0.1524" layer="91"/>
<label x="81.28" y="109.22" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="SCL"/>
<wire x1="144.78" y1="109.22" x2="152.4" y2="109.22" width="0.1524" layer="91"/>
<label x="147.32" y="109.22" size="1.778" layer="95"/>
</segment>
</net>
<net name="SDA1" class="0">
<segment>
<pinref part="U$11" gate="G$1" pin="SDA1"/>
<wire x1="76.2" y1="111.76" x2="86.36" y2="111.76" width="0.1524" layer="91"/>
<label x="81.28" y="111.76" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$6" gate="G$1" pin="SDA"/>
<wire x1="144.78" y1="111.76" x2="152.4" y2="111.76" width="0.1524" layer="91"/>
<label x="147.32" y="111.76" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<plain>
</plain>
<instances>
</instances>
<busses>
</busses>
<nets>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
