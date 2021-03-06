# -*- coding: utf-8 -*-
"""Episode: 4.真実
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_realher(w: World):
    yuri, kudo, jas = w.get("yuri"), w.get("kudo"), w.get("jas")
    chen = w.get("chen")
    return w.scene("本当の彼女",
            w.cmd.change_stage("library"),
            w.cmd.change_date("voyagetown"),
            w.cmd.change_time("midmorning"),
            w.symbol("　　　　９"),
            yuri.do("この街に入ってから五日、主だった施設の調査も終え、$Sは$kudoと共に図書館を訪れた",
                "そろそろこの場所に別れを告げる時が迫っている",
                "今日もおそらく$exfull_andreは戻ってこない"),
            kudo.talk("おそらく、というのは僅かな可能性がある時に使う言葉だ", "確率はゼロだ、$yuri"),
            yuri.talk("分かっているよ", "けれどもしも、という場合だってあるだろう？"),
            kudo.talk("もしもは無い", "ゼロだ"),
            yuri.talk("分かったよ"),
            yuri.do("頑固な犬型ドローンに小さく首を振り、$Sは玄関を潜る"),
            yuri.talk("おはようございます"),
            yuri.do("今日は自分からそう言って$Sは彼女に話しかけた",
                "そのことに戸惑ったようで、視線を中空に彷徨わせ、それから付け足したように「おはようございます」と答えた",
                "最初に遭った時と同じ服装、同じ髪型、同じ眼鏡、同じ顔で、おそらくこれが彼女の当時の日常だったのだと$Sに思わせた"),
            yuri.talk("今日、$exfull_andreさんは来ますかね"),
            jas.talk("すみません", "彼は明日"),
            yuri.talk("来ませんよね","分かっています"),
            yuri.do("$Sは彼女の言葉を遮って笑みを浮かべると、ひと呼吸置いてからこう切り出した"),
            yuri.talk("実は彼、$exfull_andreという宇宙飛行士が存在しないことは数日前に確認済みでした",
                "そもそも彼が行くはずだった月面基地はもうありません",
                "月そのものが今は無いんですよ", "知りませんでしたか？"),
            jas.do("$Sは「分からない」と首を振る"),
            yuri.talk("これを見てもらえますか"),
            yuri.do("$Sが$kudoに合図をすると彼は倒れたケースの隣の白い壁に、ある映像を投影した"),
            chen.voice("ハーイ。こんにちは"),
            yuri.do("ひび割れた壁に楕円形に映し出されたのは宇宙船内で撮影された録画映像だ",
                "画面の中央で、小麦色の肌の、くるくると癖の強い毛を後ろでまとめている女性がにこやかに手を振っている"),
            chen.voice("$exfull_jasです",
                "地球を出て三日目", "明日には月面基地に向かいます"),
            yuri.do("話している言語は英語だったが、彼女にも伝わるように下に翻訳字幕が表示されている",
                "こういう細かい気遣いを$kudoが常時してくれれば良いのに、と$Sは思うのだがそれを口にすると気遣いについての講義が始まるから、いつも心の中に仕舞っておく"),
            chen.voice("宇宙から見た地球は本当に綺麗で、最近異常気象が続いていると云われていますが、全世界の人がこの光景を見れば自分たちが暮らす場所をもっと大切にしなければいけないと思ってくれるんじゃないかと、",
                "$meは期待をしています"),
            yuri.do("映像を撮影しているカメラの向きを少し右にズラすと、丸い窓から小さく青と白の惑星が見えた",
                "映像でしか見たことのない昔の地球の姿だ", "$yuriの前で彼女はそれを自分の口元に両手をやりながら黙って見つめている"),
            chen.explain("宇宙飛行士の$jasは続けて船内でどんな暮らしをしているか、月面基地での任務への意気込み、それに地球に残した家族や友人たちへの言葉を、笑みを浮かべて話した",
                "それらはホームビデオのような呑気さで、基地に到着して半年もしない内に誰も予想し得なかった大災害によりその生涯を終えるとは思えない明るさに満ちていた"),
            chen.voice("宇宙飛行士になるのは$meの一つの夢でした",
                "あまり裕福ではない家庭で、満足に本も買えず、それでも何とか勉強したくて図書館に通った日々を今でも忘れることはできません",
                "それでも諦めない限り、夢は手が届くところまで近づけることは可能なんです",
                "$meは夢を掴むまでに本当に沢山の人にお世話になりました", "家族や学校、大学の先生、先輩、同級生たち", "他にも沢山います",
                "一人一人に今ここで感謝を述べる時間はありませんけれど、本当に心からお礼と感謝を言わせて下さい"),
            jas.do("じっと彼女の言葉に耳を傾けていた$jasだったが、使っている言語が突然現地語に変わり、はっとしたように声を漏らした"),
            chen.voice("最後にもう一人だけ、$meが宇宙飛行士になるのにお世話になった彼女に伝えてもいいでしょうか？",
                "図書館司書のリーナさん", "ねえ、リーナ。元気にしてる？", "約束の本はちゃんと取ってあるかしら"),
            jas.talk("はい"),
            chen.voice("そろそろモスクの前に植えた花が咲いている頃かしらね", "もし咲いていたら、ちゃんと写真を取っておいてね"),
            jas.do("ジャスミンではない", "リーナは目に涙を溜めて、映像の中で手を振るジャスミンに同じように手を振り返している", "その手が、指先から光の粒に変化していく"),
            kudo.talk("崩壊現象だ"),
            kudo.do("$kudoがわざわざ言葉にしたが、"),
            yuri.talk("知っているよ"),
            yuri.do("$Sは小さく言って、それから先の言葉を遮った"),
            yuri.do("彼らの見ている前でリーナの全身が光り、それが明滅を繰り返しながら徐々に空気に溶けるように淡くなっていく",
                "その瞳から、光の雫が零れた",
                "幽霊に意思はない、と云われている",
                "けれど$Sを見て彼女は一度頭を下げた", "それから声にはならなかったが「Terima kasih」と口を動かすと、",
                "そのまま光の粒になり、霧散してしまった"),
            kudo.talk("雨が降り始めた"),
            yuri.talk("そうみたいだね、$kudo"),
            yuri.do("完全に彼女が消えてしまうと、$Sは外に確認に向かった$kudoを放っておいて一人ケースの中の本を手に取った",
                "カバーが歪み、紙の上下が変色していたが、中の文章には目立った汚れはない"),
            yuri.do("数ページを確認するように捲ると、興味を失ったかのようにそっと本を閉じた"),
            )

def sc_readbook_onroad(w: World):
    yuri, kudo, jas = w.get("yuri"), w.get("kudo"), w.get("jas")
    return w.scene("そして本を読む",
            w.cmd.change_stage("street"),
            w.cmd.change_time("afternoon"),
            w.symbol("　　　　１０"),
            yuri.do("鬱蒼とした森だな、と$Sは唇を引き締める"),
            yuri.do("蔦が絡まった樹木が立ち並び、足元には動物が通った跡すら見えない",
                "頭上を覆うのは空ではなく茂った葉で、光の加減か黒く染まったものが蠢いているようにも見えた",
                "一メートル先を四つの足を器用に動かしながら進む$kudoは特に苦を感じている様子はない",
                "自分も四足歩行ならもっと楽に歩けるのだろうか、と考えながら$Sは最近動かす度に金属の摩擦を感じるようになった右足を持ち上げる"),
            yuri.do("ジャスミン・シティ、と名付けた街を出てもう四日", "次の未登録地区はまだ見えない"),
            kudo.talk("ユーリィ", "何故あの本を押収しなかったのかね"),
            yuri.talk("説明しただろ、クド",
                "本が一冊でもあればあそこは図書館でいられる", "それに本の中身があれば入れ物は要らないんじゃないかな"),
            kudo.talk("記録士としてあるまじき発言だと思われる"),
            yuri.talk("それじゃあ今の発言は削除"),
            kudo.talk("了解した"),
            yuri.do("あの本はかつてロシアという国で生まれた作家の、短編集だった",
                "それにパッキング処理を施しガラスケース内に戻しておいたのは、リーナが言ったあの言葉が気に入ったからだ"),
            yuri.talk("クド", "どうして人間にはかつて”思い”なんてものがあったのだろうか"),
            kudo.talk("それは質問か？", "それなら心理学や社会学からの引用を"),
            yuri.talk("$meや$kudoには一生理解できないものかもね"),
            yuri.do("自嘲して、自分の人工皮膚の手を握り締める"),
            yuri.explain("ユーリィは人間、ではなかった",
                "記憶を転写した脳素子を搭載する探索用人型ドローンだ", "汚れた空気の中で呼吸をし、誰も生きていない世界を見て回る",
                "僅かに残った人間たちがいつか再びこの世界で空を見上げられる時の準備をする為の調査の一環だった"),
            yuri.talk("クド", "あそこで今夜は休もう"),
            yuri.do("その視線の先にあったのは、屋根があるだけのバス停だった"),
            yuri.do("背もたれの剥がれたベンチに寝転び、軒先から空を見上げる"),
            kudo.talk("あまり衛星通信には向かない空模様だ"),
            yuri.talk("$kudo、それはジョークかい？", "いつも$meらが見上げる空はこんなものじゃないか"),
            yuri.do("その通りだ、と答えた$kudoは$Sが寝転ぶベンチの下側に入り、蹲っている",
                "どちらの意味で言ったのだろうか訊くべきだろうかと考えたが、彼は話を続けるつもりはないようなのでそのまま黙っておいた"),
            yuri.do("$Sはダウンロードしておいたあの本の中の一編『かわいい女』をゴーグルに呼び出して、そのページを開く", "&"),
            yuri.do("オーレンカという女性が夫と夫の仕事や趣味を愛して自分も没頭していくが、不幸なことに次々と夫や愛する男は旅立ってしまう",
                "その生き方に彼女の主体性はなく、ただ思いだけがある",
                "そんな女の半生の物語だった"),
            w.symbol("（了）"),
            )

## episode
def ep_truth(w: World):
    return w.episode("真実",
            # add scenes
            sc_realher(w),
            sc_readbook_onroad(w),
            outline="4.彼が帰って来ないことをジャスミンに伝え、その事情を彼女に教える。彼女はジャスミンではなかった",
            )
