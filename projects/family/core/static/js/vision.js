        var cookie_prefix="gsr_blind_";
        function createCookie(name, value, expires) {
            if (!expires){
                var days=356;
                var expires = new Date();
                expires.setDate(expires.getDate() + days);
            }
            document.cookie = name+"="+value+"; expires="+expires.toGMTString()+";path=/";
        }
        function setCookie(name, value, expires, path, domain, secure) {
            if (!name || !value) return false;
            var str = name + '=' + encodeURIComponent(value);

            if (expires) str += '; expires=' + expires.toGMTString();
            if (path)    str += '; path=' + path;
            if (domain)  str += '; domain=' + domain;
            if (secure)  str += '; secure';

            document.cookie = str;
            return true;
        }
        function readCookie(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');
            for(var i=0;i < ca.length;i++) {
                    var c = ca[i];
                    while (c.charAt(0)==' ') c = c.substring(1,c.length);
                    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
            }
            return null;
        }

        function eraseCookie(name) {
            createCookie(name,"",new Date(0));
        }

        $(document).ready(function() {
            var fs = readCookie(cookie_prefix+"fs");
            if (typeof fs === undefined) {
                    fs = 'normal_fs';
                }
                $("body").addClass(fs);
                $("input:radio[name|='font_size[]']").each(function (i) {
                    if (this.id+'_fs' == fs) {
                        $(this).prop("checked", "checked");
                    } else {
                        $(this).removeAttr("checked");
                    }
                });

            var bg = readCookie(cookie_prefix+"bg");
            if (typeof bg === undefined) {
                    bg = 'standart_bg';
                }
                $("body").addClass(bg);
                $("input:radio[name|='bg[]']").each(function (i) {
                    if (this.id+'_bg' == bg) {
                        $(this).prop("checked", "checked");
                    } else {
                        $(this).removeAttr("checked");
                    }
                });
            var kern = readCookie(cookie_prefix+"kern");
            if (typeof kern === undefined) {
                    kern = 'normal_kern';
                }
                $("body").addClass(kern);
                $("input:radio[name|='kern[]']").each(function (i) {
                    if (this.id+'_kern' == kern) {
                        $(this).prop("checked", "checked");
                    } else {
                        $(this).removeAttr("checked");
                    }
                });
            var au = readCookie(cookie_prefix+"au");
            if (typeof au === undefined) {
                    au = 'off_au';
                }
                $("body").addClass(au);
                $("input:radio[name|='au[]']").each(function (i) {
                    if (this.id+'_au' == au) {
                        $(this).prop("checked", "checked");
                    } else {
                        $(this).removeAttr("checked");
                    }
                });

        var playing = false;
        $('.audio_play').bind('click', function () {
                $('audio').trigger('pause');
            $('#audio' + this.value).trigger('play');

            })

        $(".clear_vision").bind('click', function () {
            document.cookie = "gsr_blind_bg=; expires=" + new Date(0) + ";path=/";
            document.cookie = "gsr_blind_kern=; expires=" + new Date(0) + ";path=/";
            document.cookie = "gsr_blind_fs=; expires=" + new Date(0) + ";path=/";
            document.cookie = "gsr_blind_au=; expires=" + new Date(0) + ";path=/";
            $('body').removeClass('black_bg white_bg large_kern huge_kern large_fs huge_fs on_au off_au');
            $('a.starblind').filter(':hidden').removeClass('hidden');
            $("input:radio[name|='kern[]']").each(function (i) {
                if (i == 0) {
                    $(this).attr("checked", "checked");
                } else {
                    $(this).removeAttr("checked");
                }
            });
            $("input:radio[name|='bg[]']").each(function (i) {
                if (i == 0) {
                    $(this).attr("checked", "checked");
                } else {
                    $(this).removeAttr("checked");
                }
            });
            $("input:radio[name|='font_size[]']").each(function (i) {
                if (i == 0) {
                    $(this).attr("checked", "checked");
                } else {
                    $(this).removeAttr("checked");
                }
            });
            $("input:radio[name|='au[]']").each(function (i) {
                if (i == 0) {
                    $(this).attr("checked", "checked");
                } else {
                    $(this).removeAttr("checked");
                }
            });

        });


        $("input:radio[name|='kern[]']").each(function(){
            $(this).bind('change', function() {
                var classes="normal_kern large_kern huge_kern";
                $("body").removeClass(classes);
                var cookie_name = cookie_prefix + "kern";
                eraseCookie(cookie_name);
                $("body").addClass(this.id+"_kern");
                createCookie(cookie_name, this.id+"_kern");
            });
        });

        $("input:radio[name|='bg[]']").each(function(){
            $(this).bind('change', function() {
                var classes="white_bg black_bg";
                $("body").removeClass(classes);
                var cookie_name = cookie_prefix + "bg";
                eraseCookie(cookie_name);
                $("body").addClass(this.id+"_bg");
                createCookie(cookie_name, this.id+"_bg");
            });
        });

        $("input:radio[name|='font_size[]']").each(function(){
            $(this).bind('change', function() {
                var classes="normal_fs large_fs huge_fs";
                $("body").removeClass(classes);
                var cookie_name = cookie_prefix + "fs";
                eraseCookie(cookie_name);
                $("body").addClass(this.id+"_fs");
                createCookie(cookie_name, this.id+"_fs");
		});
         $("input:radio[name|='au[]']").each(function() {
             $(this).bind('change', function () {
                 var classes = "off_au on_au";
                 $("body").removeClass(classes);
                 var cookie_name = cookie_prefix + "au";
                 eraseCookie(cookie_name);
                 $("body").addClass(this.id + "_au");
                 createCookie(cookie_name, this.id + "_au");
                console.log(readCookie(cookie_name));
             });
         })
	});
});