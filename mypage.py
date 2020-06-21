
class Mypage():

    def __init__(self,page,ret,path,num=8):                              #self.n当前页码 self.x最大页码
        self.page=page
        self.ret=ret
        self.path=path
        self.num=num

        if not self.page:
            self.page = '1'
        try:
            self.n = int(self.page)
            count = self.ret.count()
            self.x, self.y = divmod(count, self.num)
            if self.y:
                self.x = self.x + 1
            if self.n > self.x:
                self.n = self.x
            if self.x==0:
                self.n=1
        except:
            self.n = 1
        self.start = self.n - 3
        self.end = self.n + 3

        if self.start < 1:
            self.start = 1
        if self.end > self.x:
            self.end = self.x

    @property
    def html(self):
        html= """<nav aria-label="Page navigation" style="float: right;margin-right: 20px">
                <ul class="pagination">"""
        for i in range(self.start-1,self.end):
            if i+1 == self.n:
                html += '<li class="active"><a href="{1}?page={0}">{0}</a></li>'.format(i + 1,self.path)
            else:
                html+='<li><a href="{1}?page={0}">{0}</a></li>'.format(i+1,self.path)

        html+="""<li>
                    <a href="{1}?page={0}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
                </ul>
            </nav>""".format(self.x,self.path)
        return html

    @property
    def result(self):
        ret = self.ret[self.n * self.num - self.num:self.n * self.num]
        return ret
