# -*- coding: utf-8 -*-
"""Episode: 2.古い図書館
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## defines
W = Writer
_ = W.getWho()

## scenes
def sc_library_lady(w: World):
    yuri, kudo, jas = W(w.yuri), W(w.kudo), W(w.jas)
    return w.scene("図書館の女性",
            w.symbol("　　　　◆"),
            yuri.do("屋上からは無事に見えたのに、図書館だという建物の玄関は大きく崩れていた"),
            _.do("中は二階までの吹き抜け構造になっていて、天井には薄っすらと宗教画のようなものが残っている",
                "ただ採光の為の窓が少なく本棚が多く並ぶ奥の部屋は暗がりに浸かっていた",
                "それでも$Sは貴重なライトを使い、それら本棚の一つ一つを確認して回る"),
            _.do("木製の棚ではなかったから棚そのものが風化しているということはなかった",
                "ただ所蔵されている本は当然紙を原料としたものであり、風雨に晒されて劣化した挙句、虫による侵食で外観のみを残して中身は空洞化してしまっていた"),
            _.do("手に取るのが躊躇われた",
                "それでも一冊くらいは、と分厚いハードカバーの装丁本を引き抜いてみたがその途端、砂になった中身が落下した"),
            _.talk("クド、ここに本が現存している確率は？"),
            kudo.talk("０．０１％程度あれば良い"),
            yuri.talk("そういう時は望み薄だ、と言ってくれ"),
            _.do("それでも本物の書籍を拝みたいという、記録士としての真っ当な気持ちで全ての本棚を調べて回ったが、残念ながらこの施設はもう図書館として名乗るべき所蔵品を持っていないことが判明しただけだった"),
            yuri.talk("クド、０％だ"),
            _.do("そう言ってやったが、犬型ドローンは頑なに「ゼロではない」と言い張る"),
            _.do("諦めて入り口の方に向かった時だった"),
            yuri.talk("いいガラスケースがある"),
            kudo.talk("素材は合成樹脂と推定"),
            yuri.do("入る時に見落としていたようだ",
                "瓦礫の陰に隠れて展示用のケースが一台、倒れていた"),
            _.do("その中に五冊の本を見つける",
                "ただ、ケースから飛び出ていた四冊は腐食していた",
                "ケースの中に唯一留まっていた一冊だけが無事なように見えた"),
            _.talk("押収するよ、クド。記録"),
            kudo.talk("了解した"),
            yuri.do("時刻と押収物を犬型ドローンに記録させる"),
            _.do("開いたケースの隙間に手を入れ、かつてペーパーバックと呼ばれていたものだろう、片手で持てる程度のサイズの本を、取った"),
            jas.talk("その本を、借りられますか？"),
            yuri.do("振り返ると、知らない眼鏡の女性が立っていた",
                "言語は英語でもドイツ語でもロシア語ですらない"),
            _.do("ユーリィはクドを見たが、その間に言語特定が終わったようで、彼女が自分にこの本のレンタルを尋ねたのだと理解した"),
            _.do("女性はユーリィとは違いかなり軽装で、脛が見える程度の長さの赤やオレンジで編み込まれたワンピースに合皮の袖なしベストを着ていた",
                "肌はミルクチョコレートのようで、後ろでまとめられた髪は艶があり黒い"),
            jas.talk("ところで、当館ではペットの持ち込みは禁じられていますので、申し訳ないのですがそちらの……"),
            yuri.talk("クドです",
                "クドリャフカというのですが長いのでクドと省略しています", "彼はあまり気に入っていないようです"),
            jas.talk("クドさんは、外に括り付けておいていただけませんか？"),
            yuri.do("犬が怖い、というのではないのだろうが、彼女はまじまじと犬型ドローンを見下ろしている"),
            _.talk("彼はペットではなく、記録用のドローンなんです"),
            jas.talk("ドローン？"),
            yuri.do("ああ、とユーリィは理解する", "それとも、やはり、という思いだろうか"),
            yuri.talk("ロボット、いえ、色々と便利な機械です", "見た目が犬の形をしているだけで"),
            jas.talk("ロボットは分かります", "なら、危険はないのですね"),
            yuri.talk("ええ。大丈夫です", "あなたに襲いかかることは決してありません",
                "それよりもこの本はとても貴重な物です", "$meらはそういったものを集めて記録、保管するのが仕事なんです", "だから、持っていっても良いでしょうか"),
            _.do("彼女は首を振る"),
            jas.talk("そちらの本には先約があります", "その方に貸し出した後でしたら、あなたにお貸しすることも可能ですけど"),
            yuri.do("困った、という表情をユーリィはクドに向けたが、彼は「コードが優先される」と短く告げた"),
            _.explain("コード、というものの存在が、ユーリィたち記録士にとっては絶対だった",
                "それは彼らの業務についての規定であり、彼らを縛り付けているルールでもあり、彼らそのものとも言えた",
                "そこには『現地に人間がいた場合、彼らの言うことを受け入れる必要がある。しかし人間でない場合においてはこの限りでない』と記されている"),
            _.do("彼女の輪郭が、戸惑いがちに動く度に微かな発光現象を起こす"),
            yuri.talk("その方というのはいつ来られるんですか？"),
            _.do("質問を返したユーリィにクドは小さく頭を振った"),
            jas.talk("明日、帰ってこられますよ。この地球に"),
            yuri.talk("というと、どこか遠い場所に？"),
            jas.talk("はい。彼はこの国を代表する宇宙飛行士です", "$exfull_andreと言います"),
            jas.explain("彼女によれば$exfull_andreなる人物は一年前に別の国にある打ち上げ基地からロケットで月に向かい、そこに建造されたステーションで様々な任務を十二ヶ月間こなした後、ここに戻ってくるらしい"),
            yuri.talk("分かりました。ではまた明日、訪ねてみます"),
            jas.talk("すみません"),
            yuri.talk("いえ。先約があるのでしたら仕方ない。そうだ。お名前を教えていただけますか？"),
            jas.talk("$exfull_andreです"),
            yuri.talk("いえ、あなたの"),
            jas.talk("$me、ですか？　$meは……ジャスミン。ジャスミン・チェンです"),
            yuri.talk("$meはユーリィ・コマロフ", "ユーリィと気軽に呼んで下さい。それでは"),
            )

## episode
def ep_old_library(w: World):
    return w.episode("古い図書館",
            # add scenes
            sc_library_lady(w),
            note="2.古い図書館には貴重な本が残っていた。しかし司書を名乗る電磁幽霊の女性が現れて、本は予約済みだと言う",
            )
