# import mysql.connector as mysql
# conn=mysql.connect(user="root",password="",host="localhost")
# cursor=conn.cursor()
# cursor.execute("use library")
# # print("success")

# def addbook():
#     bn=input("enter book name:")
#     ba=input("enter author name")
#     c=int(input("enter book code"))
#     t=int(input("total books:"))
#     q="insert into books(bname,author,bcode,total) values('"+bn+"','"+ba+"','"+str(c)+"','"+str(t)+"')"
#     cursor.execute(q)
#     conn.commit()
#     print("book added successfully")
#     main()


# def issueb():
#     n=input("enter name:")
#     r=int(input("enter reg no:"))
#     co=int(input("enter book code:"))
#     d=input("enter date:")
#     q="insert into issue(name,regno,bcode,issue_date) values('"+n+"','"+str(r)+"','"+str(co)+"','"+d+"')"
#     cursor.execute(q)
#     conn.commit()
#     print("book issued to:",n)
#     bookup(co,-1)
#     main()

# def submitb():
#     n=input("enter name:")
#     r=int(input("enter reg no:"))
#     co=int(input("enter book code:"))
#     d=input("enter date:")
#     q="insert into submit(name,regno,bcode,submit_date) values('"+n+"','"+str(r)+"','"+str(co)+"','"+d+"')"
#     cursor.execute(q)
#     conn.commit()
#     print("book submitted from:",n)
#     bookup(co,1)
#     main()

# def bookup(co,u):
#     a="select total from books where bcode=%s;"
#     data=(co,)
#     cursor.execute(a,data)
#     res=cursor.fetchone()
#     t=res[0]+u
#     q="update books set total=%s where bcode=%s;"
#     d=(t,co)
#     cursor.execute(q,d)
#     conn.commit()
#     main()

# def dbook():
#     ac=input("enter book code")
#     a="delete from books where bcode='"+ac+"'"
#     cursor.execute(a)
#     conn.commit()
#     print("delete success")
#     main()

# def dispbook():
#     a="select * from books"
#     cursor.execute(a)
#     res=cursor.fetchall()
#     for i in res:
#         print(i)
#     main()

# def search():
#      ename=input("enter name")
#      q="select * from books where bname='"+ename+"'"
#      cursor.execute(q)
#      res=cursor.fetchall()
#      for i in res:
#          print(i)

# def main():
#     print("""               
#                              LIBRARY MANAGER
#     1.ADD BOOK
#     2.ISSUE BOOK
#     3.SUBMIT BOOK
#     4.DELETE BOOK
#     5.DISPLAY BOOKS
#     6.search
#     """)
#     choice=int(input("enter ur choice: \n1:addbook\n2:issuebook\n3:submitbook\n4:deletebook\n5:display\n6:search"))
#     if(choice==1):
#         addbook()
#     elif(choice==2):
#         issueb()
#     elif(choice==3):
#         submitb()
#     elif(choice==4):
#         dbook()
#     elif(choice==5):
#         dispbook()
#     elif(choice==6):
#         search()
#     else:
#         print("wrong choice")
#     main()

# # main()

# def pswd():
#     ps=input("enter password:")
#     if ps=="py143":
#         main()
#     else:
#         print("wrong password")
#         pswd()
# pswd()






