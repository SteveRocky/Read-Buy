    var objdbConn = new ActiveXObject("ADODB.Connection");
    // DSN字符串
    var strdsn = "Driver={SQL Server};SERVER=127.0.0.1;UID=sa;PWD=sa;DATABASE=coa";
    // 打开数据源
    objdbConn.Open(strdsn);
    // 执行SQL的数据库查询
    var objrs = objdbConn.Execute("SELECT menu_name FROM basic_mainmenu");
    // 获取字段数目
    var fdCount = objrs.Fields.Count - 1;
    // 检查是否有记录
    if (!objrs.EOF){
    document.write("<table border=1><tr>");
    // 显示数据库的字段名称
    for (var i=0; i <= fdCount; i++)
    document.write("<td><b>" + objrs.Fields(i).Name + "</b></td>");
    document.write("</tr>");
    // 显示数据库内容
    while (!objrs.EOF){
    document.write("<tr>");
    // 显示每笔记录的字段
    for (i=0; i <= fdCount; i++)
    document.write("<td valign='top'>" + objrs.Fields(i).Value + "</td>");
    document.write("</tr>");
    objrs.moveNext(); // 移到下一笔记录
    }
    document.write("</table>");
    }
    else
    document.write("数据库内没有记录!<br>");
    objrs.Close(); // 关闭记录集合
    objdbConn.Close(); // 关闭数据库链接