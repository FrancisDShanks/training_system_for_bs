define(["require", "exports", "lang", "setting", "mods/ui", "mods/common/cookie", "mods/common/encrypt"],
  function(t, e, f, p, u, n, a) {
    "use strict";
    function m() {
      return seajs.data.host + "/rest/a/challenge?_=" + (new Date).getTime()
    }
    e.__esModule = !0;
    var r, c, i, s, o, l, d, h, _, v, g, x, b, y, w, $, k, T, j, C, F, N, R, I = function I(t) {
      return u.ajax(t)
    };
    function S(t, e, n) {
      n ? (e.attr("aria-invalid", "true"), t.addClass("is-error").html(n).attr("tabindex", 0).focus()) : (e.attr("aria-invalid", "false"), t.removeClass("is-error").removeAttr("tabindex").html(""))
    }
    function B(t, e) {
      this.__evts = e,
        this.$form = t,
        this.__required = ["name", "index"],
        this._init()
    }
    function D(t, e, n) {
      var i = t.name,
        s = t.value,
        a = e[i],
        r = g[i],
        o = r ? r(s, t) : "";
      if (a !== o) return e[i] = !o || !n && o,
      n || c.toggleIptMsg(u(t), o && f.getText(o)),
        o
    }
    function A(t, e) {
      this.__evts = e,
        this.$form = t,
        this._init(),
        this.reset(),
        this.__required = ["id", "pw", "ca", "term"]
    }
    function L(e) {
      var n = this,
        t = this.$box = u(r.box());
      this.__$mask = t.find("u.mask");
      var i = function i(t) {
          y.save(t),
            c.nextTick(function() {
              e(y.get(!0))
            })
        },
        s = function s(t) {
          n.__$mask.toggleClass("is-shown", t)
        };
      this.__signinForm = new x(t.find(".u-signin-form"), {
        loading: s,
        succeed: i,
        showCards: this._showForm.bind(this)
      }),
        this.__cardsForm = new v(t.find(".u-validate-form"), {
          loading: s,
          succeed: i,
          fallback: function() {
            n._showForm(null)
          }
        })
    }
    function M(t) {
      var e = $.info,
        n = $.updated;
      $.info = t,
        $.status = !!t,
        $.updated = (new Date).getTime(),
      (t ? !e || e.id !== t.id: e) && u("body").triggerHandler("userChanged", V(n))
    }
    function H() {
      n && !
        function t() {
          n.del(k, j, C),
            n.del(T, j, C)
        } (),
      $.info && M(null)
    }
    function V(t) {
      return u.extend(!0, {
          isFirstCheck: 0 === t
        },
        $)
    }
    function q(t) {
      var e = R[t];
      if (e) {
        for (var n = e.cbs,
               i = y.get(!0), s = 0, a = n; s < a.length; s++) {
          var r = a[s];
          try {
            r(i)
          } catch(o) {
            console.log(o)
          }
        }
        e.cbs = []
      }
    }
    function z(t, e) {
      var n = y.get().updated;
      if ("function" == typeof t && F.one("status", t), !e && (new Date).getTime() - n < 3e3 && "function" == typeof t) c.nextTick(function() {
        F.emit("status")
      });
      else {
        var i = seajs.data.crossDomain ? "jsonp": "json";
        F.send("status", {
          url: seajs.data.host + "/rest/a/user." + i + "?country=" + seajs.data.country + "&language=" + seajs.data.language,
          dataType: i,
          process: function(t) {
            y.save(t && t.user)
          }
        })
      }
    }
    function O(e, t, n, i) {
      if (t && 0 !== t.length) t.append(new h.SignIn(function(t) {
        e && e(t)
      }).$box);
      else {
        var s = u.shadowBox({
            id: "login-shadow-box",
            head: f.getText("LG0001"),
            content: "",
            shadowCloser: !1,
            headCloser: !1 !== i,
            closed: function(t) {
              a.distroy(),
              "function" == typeof n && n(t)
            }
          }),
          a = new h.SignIn(function(t) {
            s.triggerHandler("closeBox.ui", "succeed"),
            e && e(t)
          });
        s.find(".content-box").append(a.$box),
          s.triggerHandler("fixBox.ui")
      }
    }
    seajs.data.crossDomain && seajs.use("www/mod/iframeAjax",
      function(t) {
        I = t.ajaxFN
      }),
      function(t) {
        var s = f.loginForm;
        function a(t) {
          var e = t.card + " " + t.name;
          return t.ex ? '<div class="u-card is-disabled">' + e + '<span class="status">' + t.ex + "</span></div>": '<label class="u-card" id="card-' + t.idx + '">\n                    <input type="radio" name="index" value="' + t.idx + '">' + e + "\n                </label>"
        }
        var r = {
          4 : s.type.phone,
          5 : s.type.email
        };
        var e = '<div class="u-form-view is-valid-view">\n            <h3>' + s.validHead + '</h3>\n            <div class="u-card-name"></div>\n            <div class="u-ctrl-cell">\n                <div class="u-ipt-box">\n                    <input type="text" class="u-ipt" name="name" autocomplete="off">\n                </div>\n                <div class="u-ipt-msg"></div>\n            </div>\n            <div class="u-result-box">\n                <div id="login_error_msg" class="u-result is-error" aria-live="assertive"></div>\n            </div>\n            <div class="u-form-actions">\n                <button type="submit" class="u-btn is-full-btn u-submit-btn" disabled aria-errormessage="login_error_msg" aria-invalid="false">' + s.confirmBtn + '</button>\n                <a href="#back" class="u-link-btn" tabindex="-1">' + s.prevBtn + ' <span aria-hidden="true">&gt;</span></a>\n            </div>\n        </div>';
        t.cardName = function u(t) {
          return t ? t.card + ' <span class="name">' + t.name + "</span>": ""
        },
          t.validateForm = function c(t) {
            return function i(t) {
              var e = t.cards,
                n = t.type;
              return '<div class="u-form-view is-cards-view">\n                <h3>' + s.cardHead[0] + (r[n] || "") + s.cardHead[1] + '</h3>\n                <div class="u-card-list">' + e.map(a).join("") + '</div>\n                <div class="u-form-hint">\n                    <i class="i-info"></i>\n                    ' + s.cardHint + '\n                </div>\n                <div class="u-form-actions">\n                    <button class="u-btn is-full-btn is-next-btn" name="next" disabled>' + s.nextBtn + '</button>\n                    <a href="#cancel" class="u-link-btn" tabindex="-1">' + s.prevBtn + ' <span aria-hidden="true">&gt;</span></a>\n                </div>\n            </div>'
            } (t) + e
          };
        var h = 0;
        function n(t) {
          var e = t.is,
            n = t.ico,
            i = t.plc,
            s = t.name,
            a = t.type,
            r = t.cls,
            o = void 0 === r ? "": r,
            u = t.autoComplete,
            c = [],
            l = function f(t) {
              return "__" + t + "__" + ++h
            } ("plc");
          n && c.push('<i class="u-ico ' + n + '"></i>'),
          i && c.push('<div id="' + l + '" class="u-placeholder">' + i + "</div>");
          var d = [];
          return o && d.push(o),
            c.push('<input type="' + (a || "text") + '" class="' + d.join(" ") + '" name="' + s + '"' + (u ? ' autocomplete="off"': "") + (i ? ' aria-labelledby="' + l + '"': "") + ' aria-errormessage="' + e + '-err-msg" aria-invalid="false">'),
          '<div class="u-ipt-box' + (n ? " is-ico-ipt": "") + '">\n                ' + c.join("") + "\n            </div>"
        }
        function i(t) {
          var e = t.is;
          return '<div class="u-ctrl-cell is-' + e + '-cell">\n                ' + t.parts.join("") + '\n                <div id="' + e + '-err-msg" class="u-ipt-msg" aria-live="assertive"></div>\n            </div>'
        }
        function o(t) {
          return t.replace(/\s*\n\s*/gi, "")
        }
        t.accForm = function l() {
          return o("" + i({
              is: "acc",
              parts: [n({
                is: "acc",
                ico: "u-ico-human",
                plc: s.acc,
                name: "id",
                cls: "is-text-ipt",
                max: 50
              })]
            }) + i({
              is: "pwd",
              parts: [n({
                is: "pwd",
                ico: "u-ico-lock",
                plc: s.pwd,
                name: "pw",
                type: "password",
                cls: "is-text-ipt",
                max: 20
              })]
            }) + i({
              is: "ca",
              parts: [n({
                is: "ca",
                ico: "u-ico-shield",
                plc: s.captcha,
                name: "ca",
                cls: "is-ca-ipt is-text-ipt",
                max: 6,
                autoComplete: "off"
              }), '<div class="u-captcha-box">\n                        <img src="' + m() + '" />\n                        <i class="icon-refresh"></i>\n                    </div>']
            }) + '\n            <input type="hidden" name="loginType" class="u-login-type">\n            <div class="u-result is-error"></div>\n            ' +
            function a() {
              var t = f.getConfig("terms"),
                e = p.flags && p.flags.noGDPR_user && t.mem || t.Gdpr,
                n = e.name,
                i = e.link,
                s = "u_term_ipt";
              return '<div class="u-login-term">\n                <input id="' + s + '" name="term" type="checkbox" />\n                <label for="' + s + '">\n                    ' + f.getText("LB0129") + '<a href="' + i + '" target="_blank">' + (e === t.mem && "en" === seajs.data.language ? n: "" + (f.getText("LB0130_1") + n + f.getText("LB0130_2"))) + "</a>\n                </label>\n            </div>"
            } () + '\n            <div class="u-form-actions">\n                <button type="submit" class="u-login-submit u-btn is-full-btn" disabled>' + s.loginBtn + "</button>\n                " + s.guide + ' <a href="' + s.regUrl + '" target="_blank" otype="button" otitle="立即注册">' + s.regBtn + '</a> <a href="' + s.pwdUrl + '" target="_blank">' + s.pwdBtn + '</a>\n            </div>\n            <div class="u-form-hint">\n                <i class="i-info"></i>\n                <ul>\n                    <li>' + s.hints.join("</li><li>") + "</li>\n                </ul>\n            </div>")
        },
          t.box = function d() {
            return o('<div class="u-signin-box">\n                <form class="u-signin-form" name="signin"></form>\n                <form class="u-validate-form" name="validate"></form>\n                <div class="u-mask hide"><div class="loading"></div></div>\n            <div>')
          }
      } (r = r || {}),
      (i = c = c || {}).setupInputBox = function E(n) {
        if (!n.data("__inited")) {
          var i, e = n.find("input");
          n.data("__inited", !0).on("click",
            function(t) {
              "input" !== t.target.tagName.toLowerCase() && e.focus()
            });
          var s = function s(t) {
            var e = !!t.value;
            e !== i && (i = e, n.toggleClass("hide-placeholder", e))
          };
          e.on("input propertychange", c.delayFn(function(t) {
              s(t.target)
            },
            100)),
            s(e[0])
        }
      },
      i.toggleIptMsg = function G(t, e) {
        S(t.closest(".u-ipt-box").nextAll(".u-ipt-msg"), t, e)
      },
      i.toggleResMsg = S,
      i.nextTick = function U(t) {
        setTimeout(t, 0)
      },
      i.getIptVal = function J(t) {
        return "checkbox" === t.type ? t.checked: t.value
      },
      i.delayFn = function P(n, i, s) {
        var a;
        return function() {
          for (var t = [], e = 0; e < arguments.length; e++) t[e] = arguments[e];
          a && clearTimeout(a),
            a = setTimeout(function() {
                a = null,
                  n.apply(s, t)
              },
              i)
        }
      },
      o = s = s || {},
      l = /^[a-z0-9\-_\.]+$/i,
      d = /^[a-z0-9\-_]+$/i,
      o.isEmail = function K(t) {
        var e = t.split("@");
        if (2 !== e.length) return ! 1;
        if (!l.test(e[0])) return ! 1;
        var n = e[1].split(".");
        return ! (n.length < 2) && n.every(function(t) {
          return t && d.test(t)
        })
      },
      o.isAllNumReg = /^[0-9]+$/,
      o.isMemId = function Q(t) {
        if (12 !== t.length) return ! 1;
        var e = parseInt(t[0], 10);
        if (isNaN(e)) return ! 1;
        for (var n = 0,
               i = 0,
               s = t.split("").slice(1); i < s.length; i++) {
          var a = s[i],
            r = parseInt(a, 10);
          if (isNaN(r)) return ! 1;
          n += r
        }
        return n % 7 === e
      },
      _ = h = e.forms || (e.forms = {}),
      B.prototype.render = function(t) {
        var e;
        this.$form.html(r.validateForm(t)),
          this._init();
        for (var n = this.__cards = {},
               i = 0,
               s = t.cards; i < s.length; i++) {
          var a = s[i];
          n[a.idx] = a,
          e || a.ex || (e = a)
        }
        return e && this._selectCard(e.idx),
          this._changeView(!1),
          this
      },
      B.prototype.reset = function() {
        return this.__xhr && this.__xhr.abort(),
          this.__cards = null,
          this.__index = null,
          this.__status = {},
          this.$form.off(),
          this.__inited = !1,
          this
      },
      B.prototype._init = function() {
        var n = this;
        this.__inited || (this.__inited = !0, this.$form.find(".u-ipt").on("input propertychange", c.delayFn(function(t) {
            n._checkName(t.target)
          },
          200)), this.$form.on("focus", 'input[type="radio"]',
          function(t) {
            var e = t.target;
            n._selectCard(e.value)
          }).on("click", "button",
          function(t) {
            "next" === t.target.name && (t.preventDefault(), n._changeView(!0))
          }).on("click", ".u-link-btn",
          function(t) {
            switch (t.preventDefault(), t.target.hash) {
              case "#cancel":
                return c.nextTick(n.__evts.fallback);
              case "#back":
                return n._changeView(!1)
            }
          }).on("submit",
          function(t) {
            return t.preventDefault(),
              n._showResult(null),
              n._submit(),
              !1
          }))
      },
      B.prototype.show = function(t) {
        return this.$form.toggleClass("hide", !t),
          this
      },
      B.prototype._submit = function() {
        var i = this; ! this.__xhr && this._isReady() && (this.__evts.loading(!0), this.__xhr = I({
          url: seajs.data.host + "/rest/a/exchangeKeyLogin",
          method: "POST",
          cache: !1,
          data: this.$form.serializeArray().reduce(function(t, e) {
              var n = e.name,
                i = e.value;
              return t[n] = i.trim(),
                t
            },
            {
              language: seajs.data.language,
              counry: seajs.data.country
            }),
          complete: function(t, e) {
            if (i.__xhr = null, "abort" !== e) {
              i.__evts.loading(!1);
              var n = t.responseJSON;
              if (n) return n.user ? void c.nextTick(function() {
                i.__evts.succeed(n.user)
              }) : void(n.ex && i._showResult(n));
              i._showResult({
                ex: "",
                msg: f.getText("x02")
              })
            }
          }
        }))
      },
      B.prototype._selectCard = function(t) {
        var e = this.__cards;
        if (t && e[t] && !e[t].ex) {
          var n = this.__index;
          if (n !== t) {
            this.__index = t,
              this.__status.index = !0;
            var i = "is-selected",
              s = this.$form;
            n && s.find("#card-" + n).removeClass(i),
              s.find("#card-" + t).addClass(i).children("input").prop("checked", !0),
              this._allowNext()
          }
        }
      },
      B.prototype._allowNext = function() {
        this.$form.find(".is-next-btn").prop("disabled", !this.__index)
      },
      B.prototype._checkName = function(t) {
        D(t, this.__status),
          this._allowSubmit()
      },
      B.prototype._renderName = function(t) {
        var e = this.$form;
        e.find(".u-card-name").html(r.cardName(t)),
          e.find(".is-error").html("")
      },
      B.prototype._changeView = function(t) {
        var e = this.$form,
          n = "is-validate-shown";
        t ? (this._renderName(this.__cards[this.__index]), e.addClass(n), this.$form.find(".u-ipt").val("").focus()) : (e.removeClass(n), this.$form.find(".is-selected input").focus())
      },
      B.prototype._showResult = function(t) {
        var e = t || {},
          n = e.ex,
          i = e.msg;
        c.toggleResMsg(this.$form.find(".u-result"), this.$form.find(".u-submit-btn"), i || n)
      },
      B.prototype._isReady = function() {
        var e = this.__status;
        return - 1 === this.__required.findIndex(function(t) {
          return ! 0 !== e[t]
        })
      },
      B.prototype._allowSubmit = function() {
        this.$form.find(".u-submit-btn").prop("disabled", !this._isReady())
      },
      v = B,
      g = {
        id: function(t) {
          return t ? s.isAllNumReg.test(t) ? "": s.isEmail(t) ? "": "e01": "e00"
        },
        pw: function(t) {
          return t ? t.length < 6 || !s.isAllNumReg.test(t) ? "e01": "": "e00"
        },
        ca: function(t) {
          return t ? /^[a-z0-9]{4,6}$/i.test(t) ? "": "e01": "e00"
        },
        name: function(t) {
          return t ? /^\s*[a-z\s\u4E00-\u9fA5]+\s*$/i.test(t) ? "": "e01": "e00"
        }
      },
      A.prototype.show = function(t) {
        return this.$form.toggleClass("hide", !t),
          this
      },
      A.prototype.reset = function() {
        var n = this;
        this.__status = {},
        this.__xhr && this.__xhr.abort();
        var t = this.$form.html(r.accForm());
        return setTimeout(function() {
            t.find(".is-text-ipt").each(function(t, e) {
              n._handleTxtChange(e, !0),
                c.setupInputBox(u(e).parent())
            }),
              n._allowSubmit()
          },
          600),
          this
      },
      A.prototype._init = function() {
        var i = this;
        this.__inited || (this.__inited = !0, this.$form.on("submit",
          function(t) {
            return t.preventDefault(),
              i._showResult(null),
              i._submit(),
              !1
          }).on("change", "input",
          function(t) {
            var e = t.target; !
              function n(t) {
                var e = t.type;
                return "text" === e || "password" === e
              } (e) ? i.__status[e.name] = c.getIptVal(e) : i._handleTxtChange(e),
              i._allowSubmit()
          }).on("click", ".u-captcha-box",
          function(t) {
            t.preventDefault(),
              i._resetCaptcha(u(t.currentTarget))
          }))
      },
      A.prototype._resetCaptcha = function(t) { (t || this.$form.find(".u-captcha-box")).find("img").attr("src", m()),
        this.$form.find(".is-ca-ipt").val("")
      },
      A.prototype._showResult = function(t) {
        var e = t || {},
          n = e.ex,
          i = e.msg;
        c.toggleResMsg(this.$form.find(".u-result").toggleClass("is-error", !!t), this.$form.find(".u-login-submit"), i || n)
      },
      A.prototype._submit = function() {
        var i = this;
        if (!this.__xhr && this._isReady()) {
          this.__evts.loading(!0);
          var s = this.$form.serializeArray().reduce(function(t, e) {
              var n = e.name,
                i = e.value;
              return t[n] = i,
                t
            },
            {
              language: seajs.data.language,
              country: seajs.data.country
            });
          s.pw = a.encrypt(s.pw),
            this.__xhr = I({
              url: seajs.data.host + "/rest/a/login",
              method: "POST",
              cache: !1,
              data: s,
              complete: function(t, e) {
                if (i.__xhr = null, "abort" !== e) {
                  i.__evts.loading(!1);
                  var n = t.responseJSON;
                  if (n) return n.user ? void c.nextTick(function() {
                    i.__evts.succeed(n.user)
                  }) : n.cards ? void c.nextTick(function() {
                    i.__evts.showCards({
                      cards: n.cards,
                      type: s.loginType
                    })
                  }) : void(n.ex && (i._showResult(n), i._resetCaptcha()));
                  i._showResult({
                    ex: "",
                    msg: f.getText("x02")
                  })
                }
              }
            })
        }
      },
      A.prototype._handleTxtChange = function(t, e) { !
        function i(t) {
          var e = c.getIptVal(t),
            n = ("" + e).trim();
          n !== e && (t.value = n)
        } (t),
        D(t, this.__status, e),
      "id" === t.name && this.$form.find(".u-login-type").val(function n(t) {
        if (t) {
          if (s.isAllNumReg.test(t)) return s.isMemId(t) ? "1": "4";
          if (s.isEmail(t)) return "5"
        }
        return ""
      } (t.value))
      },
      A.prototype._isReady = function() {
        var e = this.__status;
        return - 1 === this.__required.findIndex(function(t) {
          return ! 0 !== e[t]
        })
      },
      A.prototype._allowSubmit = function() {
        this.$form.find(".u-login-submit").prop("disabled", !this._isReady())
      },
      x = A,
      L.prototype._showForm = function(t) {
        t ? (this.__signinForm.show(!1), this.__cardsForm.show(!0).reset().render(t)) : (this.__cardsForm.show(!1), this.__signinForm.reset().show(!0))
      },
      L.prototype.reset = function() {
        this._showForm(null),
          this.__cardsForm.reset(),
          this.__signinForm.reset()
      },
      L.prototype.distroy = function() {
        this.$box && (this.$box.remove(), this.__$mask = null, this.reset(), this.__signinForm = null, this.__cardsForm = null)
      },
      b = L,
      _.SignIn = b,
      w = y = y || {},
      $ = {
        info: null,
        updated: 0,
        status: !1
      },
      k = "cs1246643xde",
      T = "cs1246643sso",
      j = "/",
      C = "csair.com",
      w.save = M,
      w.clear = function W(t) {
        t ? setTimeout(H, t) : H()
      },
      w.copy = V,
      w.get = function X(t) {
        return t ? V($.updated) : $
      },
      w.getStatus = function Y() {
        return $.status
      },
      N = F = F || {},
      R = {
        status: {
          xhr: null,
          cbs: []
        },
        logout: {
          xhr: null,
          cbs: []
        }
      },
      N.one = function Z(t, e) {
        var n = R[t];
        if (n) {
          var i = n.cbs; - 1 === i.findIndex(function(t) {
            return e === t
          }) && i.push(e)
        }
      },
      N.emit = q,
      N.send = function tt(e, n) {
        var i = R[e];
        if (i) {
          if (i.xhr) return;
          i.xhr = u.ajax({
            url: n.url,
            method: n.method || "get",
            dataType: n.dataType || "json",
            cache: !1,
            data: n.data,
            complete: function(t) {
              n.process && n.process(t.responseJSON, t),
                q(e),
                i.xhr = t = null
            }
          })
        }
      },
      e.logout = function et(t) {
        var e = seajs.data.crossDomain ? "jsonp": "json";
        F.one("logout",
          function() {
            y.clear(),
            "function" == typeof t && t()
          }),
          F.send("logout", {
            url: seajs.data.host + "/rest/a/logout." + e,
            dataType: e
          }),
          setTimeout(function() {
              F.emit("logout")
            },
            1e3)
      },
      e.check = z,
      e.login = O,
      e.insetForms = function nt(t, e) {
        t.html('<div class="u-static-box"><h2>' + f.getText("LG0001") + '</h2><div class="u-content-box"></div></div>').find(".u-content-box").append(new h.SignIn(function(t) {
          e && e(t)
        }).$box)
      },
      e.getUser = y.copy,
      e.getStatus = y.getStatus,
      e.getUserName = function it() {
        var t = y.get().info;
        return t && t.name || ""
      },
      e.requireLogin = function st(e, n) {
        function i(t) {
          t.status ? setTimeout(function() {
              return e(t)
            },
            0) : O(i, null, n)
        }
        var t = y.get();
        t.status ? i(t) : 0 === t.updated ? z(i) : O(i, null, n)
      }
  });
