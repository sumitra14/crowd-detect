import sqlite3
def connect_to_database(airport_name,current_time,current_day):
    conn=sqlite3.connect(r'projectdb')
    conn.execute('create table if not exists airport(airport_name text,arrival_time text,arrival_day text,terminal_name text)')
    a=conn.execute('select * from airport')
    b=a.fetchall()
    if(len(b)==0):
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','12:20','saturday','Sahar Terminal')")
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','13:00','monday','Santacruz Terminal')")
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','17:40','tuesday','Sahar Terminal')")
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','8:10','saturday','Santacruz Terminal')")
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','10:30','saturday','Santacruz Terminal')")
        conn.execute("insert into airport values('chhatrapati shivaji maharaj international airport,mumbai','10:10','sunday','Terminal-3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','12:10','sunday','Terminal 3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','12:10','sunday','Terminal 3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','13:10','sunday','Terminal 3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','15:35','friday','Terminal 2')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','8:10','monday','Terminal 3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','12:10','sunday','Terminal 2')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','20:10','saturday','Terminal 3')")
        conn.execute("insert into airport values('indira gandhi international airport,delhi','10:10','monday','Terminal 3')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','12:10','sunday','Terminal-1')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','14:20','sunday','Terminal-1')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','8:10','monday','Terminal-1')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','19:10','sunday','Terminal-2')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','12:10','monday','Terminal-2')")
        conn.execute("insert into airport values('kempegowda international airport,banglore','11:10','wednesday','Terminal-1')")
        conn.commit()
    difference=conn.execute("select arrival_time from airport where (cast(substr(arrival_time,1,2) as int)-cast(substr('%s',1,2) as int)) between %d and %d"%(current_time,1,3))
    f=difference.fetchall()
    print(f)
    v=[]
    for i in f:
        for j in i:
            v.append(j)
    print(v)
    query="select count(*),terminal_name from airport where airport_name='%s' and arrival_day='%s' and arrival_time in (%s) group by terminal_name"%(airport_name,current_day,','.join('?' for i in v))
    n=conn.execute(query,v)
    m=n.fetchall()
    conn.close()
    return m
        
        
        
        
