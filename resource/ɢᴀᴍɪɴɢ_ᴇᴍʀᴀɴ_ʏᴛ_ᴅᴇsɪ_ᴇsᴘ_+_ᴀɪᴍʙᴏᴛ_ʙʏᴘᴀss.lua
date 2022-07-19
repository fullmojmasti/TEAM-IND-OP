function setvalue(address,flags,value) local tt={} tt[1]={} tt[1].address=address tt[1].flags=flags tt[1].value=value gg.setValues(tt) end
function setvalue(address,flags,value)  local refinevalues={}  refinevalues[1]={}  refinevalues[1].address=address  refinevalues[1].flags=flags  refinevalues[1].value=value  gg.setValues(refinevalues)  end
function split(szFullString, szSeparator) local nFindStartIndex = 1 local nSplitIndex = 1 local nSplitArray = {} while true do local nFindLastIndex = string.find (szFullString, szSeparator, nFindStartIndex) if not nFindLastIndex then nSplitArray[nSplitIndex] = string.sub(szFullString, nFindStartIndex, string.len (szFullString)) break end nSplitArray[nSplitIndex] = string.sub (szFullString, nFindStartIndex, nFindLastIndex - 1) nFindStartIndex = nFindLastIndex + string.len (szSeparator) nSplitIndex = nSplitIndex + 1 end return nSplitArray end function xgxc(szpy, qmxg) for x = 1, #(qmxg) do xgpy = szpy + qmxg[x]["offset"] xglx = qmxg[x]["type"] xgsz = qmxg[x]["value"] xgdj = qmxg[x]["freeze"] if xgdj == nil or xgdj == "" then gg.setValues({[1] = {address = xgpy, flags = xglx, value = xgsz}}) else gg.addListItems({[1] = {address = xgpy, flags = xglx, freeze = xgdj, value = xgsz}}) end xgsl = xgsl + 1 xgjg = true end end function xqmnb(qmnb) gg.clearResults() gg.setRanges(qmnb[1]["memory"]) gg.searchNumber(qmnb[3]["value"], qmnb[3]["type"]) if gg.getResultCount() == 0 then gg.toast(qmnb[2]["name"] .. "开启失败") else gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) if gg.getResultCount() == 0 then gg.toast(qmnb[2]["name"] .. "开启失败") else sl = gg.getResults(999999) sz = gg.getResultCount() xgsl = 0 if sz > 999999 then sz = 999999 end for i = 1, sz do pdsz = true for v = 4, #(qmnb) do if pdsz == true then pysz = {} pysz[1] = {} pysz[1].address = sl[i].address + qmnb[v]["offset"] pysz[1].flags = qmnb[v]["type"] szpy = gg.getValues(pysz) pdpd = qmnb[v]["lv"] .. ";" .. szpy[1].value szpd = split(pdpd, ";") tzszpd = szpd[1] pyszpd = szpd[2] if tzszpd == pyszpd then pdjg = true pdsz = true else pdjg = false pdsz = false end end end if pdjg == true then szpy = sl[i].address xgxc(szpy, qmxg) end end if xgjg == true then gg.toast(qmnb[2]["name"] .. "开启成功，一共修改" .. xgsl .. "条数据") else gg.toast(qmnb[2]["name"] .. "未搜索到数据，开启失败") end end end end function SearchWrite(Search, Write, Type) gg.clearResults() gg.setVisible(false) gg.searchNumber(Search[1][1], Type) local count = gg.getResultCount() local result = gg.getResults(count) gg.clearResults() local data = {} local base = Search[1][2] if (count > 0) then for i, v in ipairs(result) do v.isUseful = true end for k=2, #Search do local tmp = {} local offset = Search[k][2] - base local num = Search[k][1] for i, v in ipairs(result) do tmp[#tmp+1] = {} tmp[#tmp].address = v.address + offset tmp[#tmp].flags = v.flags end tmp = gg.getValues(tmp) for i, v in ipairs(tmp) do if ( tostring(v.value) ~= tostring(num) ) then result[i].isUseful = false end end end for i, v in ipairs(result) do if (v.isUseful) then data[#data+1] = v.address end end if (#data > 0) then local t = {} local base = Search[1][2] for i=1, #data do for k, w in ipairs(Write) do offset = w[2] - base t[#t+1] = {} t[#t].address = data[i] + offset t[#t].flags = Type t[#t].value = w[1] if (w[3] == true) then local item = {} item[#item+1] = t[#t] item[#item].freeze = true gg.addListItems(item) end end end gg.setValues(t) gg.toast("开启成功，一共修改"..#t.."条数据") gg.addListItems(t) else gg.toast("未搜索到数据，开启失败", false) return false end else gg.toast("Not Found") return false end end
function split(szFullString, szSeparator) local nFindStartIndex = 1 local nSplitIndex = 1 local nSplitArray = {} while true do local nFindLastIndex = string.find(szFullString, szSeparator, nFindStartIndex) if not nFindLastIndex then nSplitArray[nSplitIndex] = string.sub(szFullString, nFindStartIndex, string.len(szFullString)) break end nSplitArray[nSplitIndex] = string.sub(szFullString, nFindStartIndex, nFindLastIndex - 1) nFindStartIndex = nFindLastIndex + string.len(szSeparator) nSplitIndex = nSplitIndex + 1 end return nSplitArray end function xgxc(szpy, qmxg) for x = 1, #(qmxg) do xgpy = szpy + qmxg[x]["offset"] xglx = qmxg[x]["type"] xgsz = qmxg[x]["value"] gg.setValues({[1] = {address = xgpy, flags = xglx, value = xgsz}}) xgsl = xgsl + 1 end end function xqmnb(qmnb) gg.clearResults() gg.setRanges(qmnb[1]["memory"]) gg.searchNumber(qmnb[3]["value"], qmnb[3]["type"]) if gg.getResultCount() == 0 then gg.toast(qmnb[2]["name"] .. "") else gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) gg.refineNumber(qmnb[3]["value"], qmnb[3]["type"]) if gg.getResultCount() == 0 then gg.toast(qmnb[2]["name"] .. "") else sl = gg.getResults(999999) sz = gg.getResultCount() xgsl = 0 if sz > 999999 then sz = 999999 end for i = 1, sz do pdsz = true for v = 4, #(qmnb) do if pdsz == true then pysz = {} pysz[1] = {} pysz[1].address = sl[i].address + qmnb[v]["offset"] pysz[1].flags = qmnb[v]["type"] szpy = gg.getValues(pysz) pdpd = qmnb[v]["lv"] .. ";" .. szpy[1].value szpd = split(pdpd, ";") tzszpd = szpd[1] pyszpd = szpd[2] if tzszpd == pyszpd then pdjg = true pdsz = true else pdjg = false pdsz = false end end end if pdjg == true then szpy = sl[i].address xgxc(szpy, qmxg) xgjg = true end end if xgjg == true then gg.toast(qmnb[2]["name"] .. "" .. xgsl .. "") else gg.toast(qmnb[2]["name"] .. "") end end end end
function setvalue(address,flags,value) local tt={} tt[1]={} tt[1].address=address tt[1].flags=flags tt[1].value=value gg.setValues(tt) end
function setvalue(address,flags,value) local tt={} tt[1]={} tt[1].address=address tt[1].flags=flags tt[1].value=value gg.setValues(tt) end
function setvalue(address,flags,value) local tt={} tt[1]={} tt[1].address=address tt[1].flags=flags tt[1].value=value gg.setValues(tt) end
function setvalue(address,flags,value)  local refinevalues={}  refinevalues[1]={}  refinevalues[1].address=address  refinevalues[1].flags=flags  refinevalues[1].value=value  gg.setValues(refinevalues)  end

function IMRAN()
YT = gg.multiChoice({
"\n╔━━━━━━━━━━━━━━━━━━━╗ \n •3ʀᴅ ᴘᴀʀᴛʏ ʙʏᴘᴀss 8-10  ✨ᴮʸ ɪᴍʀᴀɴ \n ╚━━━━━━━━━━━━━━━━━━━╝",---1
"\n╔━━━━━━━━━━━━━━━━━━━╗ \n •ʟᴏʙʙʏ ʙʏᴘᴀss [ʟᴏʙʙʏ] ✨ᴮʸ ɪᴍʀᴀɴ \n ╚━━━━━━━━━━━━━━━━━━━╝",---2
"\n╔━━━━━━━━━━━━━━━━━━━╗ \n •ᗴxɪᴛ     [ ʙʏ ɪᴍʀᴀɴ ᴏᴘ ]  ✨ᴮʸ ɪᴍʀᴀɴ\n ╚━━━━━━━━━━━━━━━━━━━╝",---3
  }, nil, "🌺 ᴜsᴇ ᴏɴʟʏ ᴅᴇsɪ ᴇsᴘ + ᴀɪᴍʙᴏᴛ ɴᴏ ʙᴀɴ 🌺")
  
if YT == nil then else gg.toast("🌺 ᴅᴇsɪ ᴇsᴘ + ᴀɪᴍʙᴏᴛ sᴜᴘᴘᴏʀᴛ ᴏᴛʜᴇʀ ʜᴀᴄᴋ ᴜsᴇ ʙᴀɴ 🌺")

if YT[1] == true then IMR1()end
if YT[2] == true then IMR2()end
if YT[3] == true then IMRANEXIT()end
end
IMRANOP = -1
end

function IMR1()
gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.iglite.ztf", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.editAll("119", gg.TYPE_BYTE)
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.iglite", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.editAll("119", gg.TYPE_BYTE)
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.mmm", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.editAll("119", gg.TYPE_BYTE)
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.iglitece", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.editAll("119", gg.TYPE_BYTE)
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.mobileqqq", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.editAll("119", gg.TYPE_BYTE)
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.iglite.qq", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.editAll("119", gg.TYPE_BYTE)
 gg.clearResults()
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
 gg.setRanges(gg.REGION_C_ALLOC)
 gg.searchNumber(":com.tencent.iglite.ztf", gg.TYPE_BYTE)
 gg.getResults(50000)
 gg.editAll("119", gg.TYPE_BYTE) 
 gg.toast("👑 ɢᴀᴍɪɴɢ ᴇᴍʀᴀɴ ʏᴛ 👑")
------------------------------------------
gg.alert("💮3ʀᴅ ᴘʀᴛʏ ғɪx ᴀᴄᴛɪᴠᴛᴇᴅ 6/10💮")
end

function IMR2()
gg.setRanges(gg.REGION_C_ALLOC | gg.REGION_OTHER)
gg.searchNumber("572854148005888;579451217772544")
gg.refineNumber("572854148005888")
gg.getResults(50000)
gg.editAll("361418272522109953", gg.TYPE_QWORD)
gg.clearResults()
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC | gg.REGION_OTHER)
gg.searchNumber("577252194516992;582749752655872")
gg.refineNumber("577252194516992")
gg.getResults(50000)
gg.editAll("361418272522109953", gg.TYPE_QWORD)
gg.clearResults()
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC | gg.REGION_OTHER)
gg.searchNumber("573953659633664;578351706144768")
gg.refineNumber("573953659633664")
gg.getResults(50000)
gg.editAll("361418272522109953", gg.TYPE_QWORD)
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC | gg.REGION_OTHER)
gg.searchNumber("578351706144768;564058054983680")
gg.refineNumber("578351706144768")
gg.getResults(50000)
gg.editAll("361418272522109953", gg.TYPE_QWORD)
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC | gg.REGION_OTHER)
gg.searchNumber("620137442967552;564058054983680")
gg.refineNumber("620137442967552")
gg.getResults(50000)
gg.editAll("361418272522109953", gg.TYPE_QWORD)

gg.searchNumber("133378;144387", gg.TYPE_DWORD)
gg.refineNumber("133378", gg.TYPE_DWORD)
gg.getResults(50000)
gg.editAll("67109633", gg.TYPE_DWORD)
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("134658;262403", gg.TYPE_DWORD)
gg.refineNumber("134658", gg.TYPE_DWORD)
gg.getResults(50000)
gg.editAll("67109633", gg.TYPE_DWORD)
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("134914;133378", gg.TYPE_DWORD)
gg.refineNumber("134914", gg.TYPE_DWORD)
gg.getResults(50000)
gg.editAll("67109633", gg.TYPE_DWORD)
gg.clearResults()
gg.alert("ʟᴏʙʙʏ ʙʏᴘᴀss ᴅᴏɴᴇ ✅ \n\n\n\n ᴘʀɪᴠᴀᴛᴇ ʙʏᴘᴀss ᴇɴᴊᴏʏ ") 
end

----------------------------------------------------------

function IMRANEXIT()
  print("┗❏: ᴄʀᴇᴅɪᴛ ʙʏ @ɢᴀᴍɪɴɢ_ᴇᴍʀᴀɴ_ʏᴛ_ᴏᴡɴᴇʀ ᴠɪᴘ sᴄʀɪᴘᴛ\n┗❏: ᴊᴏɪɴ ᴛᴇʟʀɢʀᴀᴍ @ɢᴀᴍɪɴɢ_ᴇᴍʀᴀɴ_ʏᴛ_ᴏᴡɴᴇʀ\n┗❏: 🇮🇳 ᴍʏ sᴄʀɪᴘᴛ ᴘᴀɪᴅ sᴄʀɪᴘᴛ 🇮🇳\n┗❏: ᴘᴀɪᴅ ʜᴀᴄᴋ ʙᴜʏ  ᴡᴀᴛsʜᴜᴘ ɴᴜᴍʙᴇʀ 9759769417")
  gg.skipRestoreState()
  os.exit()
end
while true do
  if gg.isVisible(true) then
    IMRANOP = 1
    gg.setVisible(false)
  end
  if IMRANOP == 1 then
    IMRAN()
  end
end