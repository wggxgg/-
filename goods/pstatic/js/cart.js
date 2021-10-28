    $(function(){
        var ul=$('#list-cont ul');
        //总价
        var total = $('.pieces-total');
        var check =$('.CheckBoxShop');
        var add = $('.add');
        var less = $('.less');
        //全选
        var allcheck=$('#allCheckked');
        //件数
        var selected=$(".Selected-pieces");
        var numcheck=$("#numcheck");
        //小计
        var sum=$(".sum");
        //单价
        var th_su=$(".th-su");
        //数量
        var Quantity=$(".Quantity-input");
        for (var i=0;i<check.length;i++){
            console.log( th_su[i].innerText);
            console.log( $(Quantity[i]).val());
            sum[i].innerText=th_su[i].innerText*$(Quantity[i]).val();
        }

        //+
        add.click(function () {
            //小计
            var sum=$(this).parents("ul").find(".sum");
            //单价
            var th_su=$(this).parents("ul").find(".th-su").text();
            //数量
            var input = $(this).parent().children("input.Quantity-input");
            var number=parseInt(input.val())+1;
            input.val(number);
            sum.text((th_su*number).toFixed(2));

        });
        //-
        less.click(function () {
             //小计
            var sum=$(this).parents("ul").find(".sum");
            //单价
            var th_su=$(this).parents("ul").find(".th-su").text();
            //数量
            var input = $(this).parent().children("input.Quantity-input");
            var number=parseInt(input.val())-1;
            if (number<0){
                number=0;
            }
            input.val(number);
            sum.text((th_su*number).toFixed(2));
        });

        //全选
        allcheck.click(function () {
            if ($(this).prop("checked") === false){
                $(this).prop("checked",false);
                check.prop("checked",false);
                numcheck.prop("checked",false);
                selected.text(0);
            }
            if($(this).prop("checked") === true){
                $(this).prop("checked",true);
                check.prop("checked",true);
                numcheck.prop("checked",true);
                selected.text(check.length);
        }
            tot();
        });
        //单选
        check.click(function(){
            //选中数
            var len= $(":checked[class='CheckBoxShop check']").length;
            //所有数
            var alllen=check.length;
            if (len<alllen){
                allcheck.prop("checked",false);
            }else if(len===alllen){
                allcheck.prop("checked",true);
            }
            if (len>0){
                 numcheck.prop("checked",true);
             }else if(len<1){
                 numcheck.prop("checked",false);
             }
            selected.text(len);
            tot();
        });

        //总价
         function tot() {
            var to = 0,a=0;
            sum.each(function (i, v) {
                if ($(this).parent().siblings(".th-chk").find(".CheckBoxShop").prop("checked")===true) {
                    to += parseFloat($(this).text());
                    to.toFixed(2);
                }
            });
            total.text(to);
         }

        //ajax删除
        $(".dele-btn").on('click',function () {
            //商品id
            var commodityid = $(this).parent().parent().find(".commodityid").text();
            var t=  $(this).parent().parent();
            $.ajax({
                url:"/shopper/delete",
                data:{'commodityid':commodityid},
                type:"GET",
                dataType:"json",
                success:function(result){
                    if (result.state==='fail'){
                        console.log("删除失败")
                    }else{
                        t.remove();
                        console.log("删除成功")
                    }
                }
            })
        });

        //ajax全部删除
        $(".batch-dele-btn").click(function () {
            var userid=$(this).siblings("#delete_all").text();
            $.ajax({
                url:"/shopper/delete",
                data:{userid:userid},
                type:"GET",
                dataType:"json",
                success:function (result) {
                    if (result.state==='fail'){
                        console.log("删除失败")
                    }else{
                        ul.remove();
                        allcheck.prop("checked",false);
                        numcheck.prop("checked",false);
                        selected.text(0);
                        total.text(0);
                        console.log("删除成功")
                    }
                }
            })
        });

    });