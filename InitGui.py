#****************************************************************************
#*                                                                          *
#*   Flamingo Tools Workbench:                                              *
#*       few tools to speed-up drawing                                      *
#*   Copyright (c) 2016 Riccardo Treu LGPL                                  *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
#*   as published by the Free Software Foundation; either version 2 of      *
#*   the License, or (at your option) any later version.                    *
#*   for detail see the LICENCE text file.                                  *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307   *
#*   USA                                                                    *
#*                                                                          *
#****************************************************************************

class flamingoToolsWorkbench ( Workbench ):
  "Test workbench object"
  #Icon= str(FreeCAD.getHomePath() + "Mod/FlamingoTools/icons/flamingo.svg")
  #import os
  #Icon = os.path.join(os.path.dirname(os.path.abspath(__file__)),"icons","flamingo.svg")
  import DraftSnap
  Icon = '''
/* XPM */
static char * image[] = 
{
"43 43 256 2",
"AA c #000000","AB c #05090F","AC c #070D15","AD c #181818",
"AE c #131F2F","AF c #202020","AG c #303030","AH c #1A3352",
"AI c #28334E","AJ c #24405F","AK c #244571","AL c #335171",
"AM c #37597B","AN c #494949","AO c #505050","AP c #5D5D5D",
"AQ c #606060","AR c #686868","AS c #707070","AT c #7F7F7F",
"AU c #2F588B","AV c #325C8D","AW c #34609B","AX c #386495",
"AY c #3465A4","AZ c #3A65A5","BA c #3A68A6","BB c #466C96",
"BC c #406998","BD c #596B92","BE c #5B7986","BF c #567792",
"BG c #4566A8","BH c #456AA9","BI c #4C66A5","BJ c #4E65AA",
"BK c #4D6BAC","BL c #4772A2","BM c #4C70AD","BN c #5365AA",
"BO c #526FAE","BP c #5D63A7","BQ c #5A65AB","BR c #5A6DAE",
"BS c #5A6DB1","BT c #5372AE","BU c #5A71AF","BV c #5A7FA6",
"BW c #5A73B0","BX c #5D79B1","BY c #6759A1","BZ c #615FB0",
"CA c #7D46AF","CB c #7454B4","CC c #7A50B5","CD c #737B85",
"CE c #6265AD", "CF c #656EB0", "CG c #6D66B0", "CH c #6174B2",
"CI c #627CB5", "CJ c #677CB8", "CK c #6D72B4", "CL c #7465B1",
"CM c #756AB1", "CN c #7A65B1", "CO c #7A8C7D", "CP c #5D81AC",
"CQ c #67828B", "CR c #6D8686", "CS c #6788A7", "CT c #6584B4",
"CU c #6782B8", "CV c #6C83BA", "CW c #748ABD", "CX c #7492B2",
"CY c #7A8CC1", "CZ c #7A92C1", "DA c #9936B5", "DB c #9939B1",
"DC c #993BB9", "DD c #A630BC", "DE c #B326BD", "DF c #B32BBE",
"DG c #B922BE", "DH c #8565B4", "DI c #876BB6", "DJ c #8D66B6",
"DK c #8B6CB7", "DL c #9466B7", "DM c #946AB8", "DN c #9B65B8",
"DO c #A565BA", "DP c #A668BC", "DQ c #AB65BB", "DR c #AC68BD",
"DS c #B366BD", "DT c #BC66BE", "DU c #C61CC0", "DV c #CC19C2",
"DW c #D216C3", "DX c #DC11C5", "DY c #E60DC7", "DZ c #EC09C8",
"EA c #FE00CB", "EB c #C565C0", "EC c #C669C2", "ED c #CC65C2",
"EE c #D266C3", "EF c #DC66C5", "EG c #E666C7", "EH c #EC65C8",
"EI c #F266C9", "EJ c #FE66CB", "EK c #BFAC33", "EL c #868D5C",
"EM c #9A9A52", "EN c #878F61", "EO c #818073", "EP c #8D9463",
"EQ c #D9B91F", "ER c #CCB229", "ES c #D2B524", "ET c #ECC20F",
"EU c #F2C50A", "EV c #FECB00", "EW c #8F8F8F", "EX c #979797",
"EY c #9F9F9F", "EZ c #AFAFAF", "FA c #B7B7B7", "FB c #8192C4",
"FC c #839AC5", "FD c #8D9ECA", "FE c #8DA4CA", "FF c #94ACC4",
"FG c #99AAD0", "FH c #98B0CC", "FI c #9CB3D2", "FJ c #A6B9D6",
"FK c #ACC0DA", "FL c #B3C5DD", "FM c #B9C9DB", "FN c #BFCEE2",
"FO c #D7D7D7", "FP c #DFDFDF", "FQ c #C6CFE4", "FR c #C5D3E5",
"FS c #CCD8E8", "FT c #D1DCEA", "FU c #D9E2EE", "FV c #DFE7F1",
"FW c #E7E7E7", "FX c #EFEFEF", "FY c #E6EBF3", "FZ c #ECF0F6",
"GA c #F7F7F7", "GB c #F2F5F9", "GC c #FEFEFE", "GD c #000000",
"GE c #FFFFFF", "GF c #000000", "GG c #000000", "GH c #000000",
"GI c #000000", "GJ c #000000", "GK c #000000", "GL c #000000",
"GM c #000000", "GN c #000000", "GO c #000000", "GP c #000000",
"GQ c #000000", "GR c #000000", "GS c #000000", "GT c #000000",
"GU c #000000", "GV c #000000", "GW c #000000", "GX c #000000",
"GY c #000000", "GZ c #000000", "HA c #000000", "HB c #000000",
"HC c #000000", "HD c #000000", "HE c #000000", "HF c #000000",
"HG c #000000", "HH c #000000", "HI c #000000", "HJ c #000000",
"HK c #000000", "HL c #000000", "HM c #000000", "HN c #000000",
"HO c #000000", "HP c #000000", "HQ c #000000", "HR c #000000",
"HS c #000000", "HT c #000000", "HU c #000000", "HV c #000000",
"HW c #000000", "HX c #000000", "HY c #000000", "HZ c #000000",
"IA c #000000", "IB c #000000", "IC c #000000", "ID c #000000",
"IE c #000000", "IF c #000000", "IG c #000000", "IH c #000000",
"II c #000000", "IJ c #000000", "IK c #000000", "IL c #000000",
"IM c #000000", "IN c #000000", "IO c #000000", "IP c #000000",
"IQ c #000000", "IR c #000000", "IS c #000000", "IT c #000000",
"IU c #000000", "IV c #000000", "IW c #000000", "IX c #000000",
"IY c #000000", "IZ c #000000", "JA c #000000", "JB c #000000",
"JC c #000000", "JD c #000000", "JE c #000000", "JF c #000000",
"JG c #000000", "JH c #000000", "JI c #000000", "JJ c #000000",
"JK c #000000", "JL c #000000", "JM c #000000", "JN c #000000",
"JO c #000000", "JP c #000000", "JQ c #000000", "JR c #000000",
"JS c #000000", "JT c #000000", "JU c #000000", "JV c #000000",
"FXGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCFGBOAYAYAZCJFNGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCFVBKDCDXEAEAEADVCCBWGBGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGBBSDYEAEAEAEAEAEAEADWCHGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCFBDEEAEAEAEAEAEAEAEAEADFCYGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCFIFIFIFIFJFTFSFTFSFSFTFSBKDGEAEAEAEAEAEAEAEAEADZBKGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCBLENEMEMEPCQCQCQCQCQCQCQBEBDAYAYAYAYDAEAEAEAEAEABGGBGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCFLCOEVEVEVEVEVEVEVEVEVEVEVEVEVERBDDBEAEAEAEAEADYBMGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCBVEQEVEVEVEVEVEVEVEVEVEVEUEOBYDXEAEAEAEAEAEADDFDGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCFRCREVEVEVEVEVEVEVEVEVESBFCAEAEAEAEAEAEAEADVCJGAGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCCXEKEVEVEVEVEVEVEVEMCSFUFBBZDGDXEADXDUCBCJFZGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCFUBBELEMEKERETEUCOFFGCGCGCFTCYAIAKBWCVFNGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCCPAUAHALAMAXBBFMGCGCGCGCGCGCANFAGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCFYAWABAAACAUFNGCGCGCGCGCGCGCAFFPGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCCTAJACAVFTGCGCGCGCGCGCGCEZAOGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGAAWAVFRGCGCGCGCGCGCGCEYAGFPGCGCGCGCGCGCFYCZGCGCGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGCFHFRGCGCGCGCGCFZASADAPFXGCGCGCGCGCGCFZBWDRCIGBGCGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGCGCGCGCGCGCGCFWAGEWFXGCFYFSFICZCVCUCTBKEFEJEFBOFTGCGCGCGCGCGCGCGCGCGCGC","GCGCGCGCGCGCGCGCGCGCGCGCGCGCAOEZFUFBAYBKCFDNDSEDEDCEEBEJEJEJEGBJBMFIFZGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCAECVBRDSEJEJEJEJEJEJDHDQEJEJEJEJEJEICECMBKFJGBGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCFYBXBPEBEJEJEJEJEJEJEJDNDLEJEJEJEJEJEJEJEJCNDODMCWGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCFTBWEEEJEJEJEJEJEJEJEJDTCNEJEJEJEJEJEJEJEJEJEJDJDJEBCWGAGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCFTBSEIEJEJEJEJEJEJEJEJEDCGEJEJEJEJEJEJEJEJEJEJEJEJDOCLDKFJGCGCGCGC", "GCGCGCGCGCGCGCGCGCFYBWEIEJEJEJEJEJEJEJEJEFCEEIEJEJEJEJEJEJEJEJEJEJEJEJEJDTCEBKGCGCGCGC", "GCGCGCGCGCGCGCGCGCCZDTEJEJEJEJEJEJEJEJEHCEEGEJEJEJEJEJEJEJEJEJEJEJEJEJEFDQBQAZGCGCGCGC", "GCGCGCGCGCGCGCGCGBBHEJEJEJEJEJEJEJEJEJBQEFEJEJEJEJEJEJEJEJEJEJEHDTDHBJBNDJDOBKGCGCGCGC", "GCGCGCGCGCGCGCGCFTCHEJEJEJEJEJEJEJEJCGEBEJEJEJEJEJEJEJEJDTDJBNBGCNDSEGEJEJDOFEGCGCGCGC", "GCGCGCGCGCGCGCGCFTCFEJEJEJEJEJEJEJDHDQEJEJEJEJEJEDDNBZAZCLDOEGEJEJEJEJEJEHBTGBGCGCGCGC", "GCGCGCGCGCGCGCGCGBBGEJEJEJEJEJEJDODLEJEJEFDOCGAZBZDNEEEJEJEJEJEJEJEJEJEJCKFSGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCCWDTEJEJEJEJDTBQDQCNBGBQDJEBEJEJEJEJEJEJEJEJEJEJEJEHCKFQGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCFVCHEIEJEJEEAZBJDHDTEHEJEJEJEJEJEJEJEJEJEJEJEJEJDTBWFSGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCFUCHEEEJEJEGEJEJEJEJEJEJEJEJEJEJEJEJEJEJEJDSBSCYFZGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCFVCIDHEFEJEJEJEJEJEJEJEJEJEJEJEJEJEJDRBMFBFVGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCFKBTBSDLDTEDEEEJEJEJEJEEDOCNBJAYFCFZGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCFUFICYCJCJAYAYAYAYCJFEFLCDATGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCATATGCGCGCGCGCGCATATGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCATATGCGCGCGCGCGCGCAPANGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCEXARGCGCGCGCGCGCFOAGAOGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCEYAQGCGCGCGCGCEXAGFOGCGCGCGCGCGCGCGCGCGCGCGCGC", "GCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCEYAQGCGCGCFXAOARGBGCGCGCGCGCGCGCGCGCGCGCGCGCGC", "XPMENDEXT"
};  
  '''
  MenuText = "Flamingo Tools WB"
  ToolTip = "Flamingo tools workbench"
  def Initialize(self):
    import CommandsEagle
    list1 = ["importPos"]
    self.appendToolbar("eagleTools",list1)
    Log ('Loading Eagle tools: done\n')
    import CommandsSpSh
    #list2=["findFirst"]
    #self.appendToolbar("spreadsheetTools",list2)
    #Log ('Loading Spreadsheet tools: done\n')
    import CommandsPolar
    list3=["drawPolygon","drawFromFile","selectSolids","queryModel","moveWorkPlane","offsetWorkPlane","rotateWorkPlane","hackedL","moveHandle","dpCalc"]
    self.appendToolbar("polarTools",list3)
    Log ('Loading Polar tools: done\n')
    import CommandsFrame
    list4=["frameIt","fillFrame","insertPath","insertSection","FrameLineManager","FrameBranchManager","spinSect","reverseBeam","shiftBeam","pivotBeam","levelBeam","alignEdge","rotJoin","alignFlange","stretchBeam","extend","adjustFrameAngle"]
    self.appendToolbar("frameTools",list4)
    Log ('Loading Frame tools: done\n')
    import CommandsPipe
    list5=["insertPipe","insertElbow","insertReduct","insertCap","insertValve","insertFlange","insertUbolt","insertPypeLine","insertBranch","insertTank","insertRoute","breakPipe","mateEdges","joinPype","flat","extend2intersection","extend1intersection","laydown","raiseup","attach2tube","point2point","insertAny"]
    self.appendToolbar("pipeTools",list5)
    Log ('Loading Pipe tools: done\n')
    menu1 = ["Frame tools"]
    menu2 = ["Pype tools"]
    menu3 = ["Eagle tools"]
    menu4 = ["Utils"]
    self.appendMenu(menu1,list4)
    self.appendMenu(menu2,list5)    
    #self.appendMenu(menu,list2)
    self.appendMenu(menu3,list1)
    self.appendMenu(menu4,list3)

  def Activated(self):
    if hasattr(FreeCADGui,"draftToolBar"):
      FreeCADGui.draftToolBar.Activated()
    if hasattr(FreeCADGui,"Snapper"):
      FreeCADGui.Snapper.show()
    FreeCAD.__activePypeLine__=None
    FreeCAD.__activeFrameLine__=None
    Msg("Created variables in FreeCAD module:\n")
    Msg("__activePypeLine__\n")
    Msg("__activeFrameLine__\n")

  def Deactivated(self):
    del FreeCAD.__activePypeLine__
    del FreeCAD.__activeFrameLine__
    Msg("flamingoTools deactivated()\n")
    Msg("Deleted variables in FreeCAD module:\n")
    Msg("__activePypeLine__\n")
    Msg("__activeFrameLine__\n")

Gui.addWorkbench(flamingoToolsWorkbench)
