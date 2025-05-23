import tkinter as tk
from tkinter import ttk


##japanese version of the champion list
champion_list = [
    "アーゴット", "アーリ", "アイバーン", "アカリ", "アクシャン", "アジール", "アッシュ", "アニー", "アニビア", "アフェリオス", "アムム", "アリスター", "アンベッサ",
    "イブリン", "イラオイ", "イレリア", "ウーコン", "ウディア", "エイトロックス", "エコー", "エズリアル", "エリス", "オーロラ", "オーン", "オラフ", "オリアナ", "オレリオン・ソル",
    "カ・サンテ", "カーサス", "カ＝ジックス", "カイ＝サ", "カサディン", "カシオペア", "カタリナ", "カミール", "カリスタ", "カルマ", "ガリオ", "ガレン", "ガングプランク", "キヤナ",
    "キンドレッド", "クイン", "クレッド", "グウェン", "グラガス", "グレイブス", "ケイトリン", "ケイル", "ケイン", "ケネン", "コーキ", "コグ＝マウ",
    "サイオン", "サイラス", "サミーラ", "ザイラ", "ザック", "ザヤ", "シェン", "シャコ", "シン・ジャオ", "シンジド", "シンドラ", "シヴァーナ", "シヴィア", "ジェイス", "ジグス",
    "ジャーヴァンIV", "ジャックス", "ジャンナ", "ジリアン", "ジン", "ジンクス", "スウェイン", "スカーナー", "スモルダー", "スレッシュ", "セジュアニ", "セト", "セナ", "セラフィーン",
    "ゼド", "ゼラス", "ゼリ", "ソナ", "ソラカ", "ゾーイ",
    "タム・ケンチ", "タリック", "タリヤ", "タロン", "ダイアナ", "ダリウス", "チョ＝ガス", "ツイステッド・フェイト", "ティーモ", "トゥイッチ", "トランドル", "トリスターナ",
    "トリンダメア", "ドクター・ムンド", "ドレイヴン",
    "ナー", "ナサス", "ナフィーリ", "ナミ", "ニーコ", "ニーラ", "ニダリー", "ヌヌ＆ウィルンプ", "ノーチラス", "ノクターン",
    "ハイマーディンガー", "バード", "パイク", "パンテオン", "ビクター", "フィオラ", "フィズ", "フィドルスティックス", "フェイ", "ブライアー", "ブラウム", "ブラッドミア", "ブランド",
    "ブリッツクランク", "ヘカリム", "ベイガー", "ベル＝ヴェス", "ボリベア", "ポッピー",
    "マオカイ", "マスター・イー", "マルザハール", "マルファイト", "ミス・フォーチュン", "ミリオ", "メル", "モルガナ", "モルデカイザー",
    "ヤスオ", "ユーミ", "ヨネ", "ヨリック",
    "ライズ", "ラカン", "ラックス", "ラムス", "ランブル", "リー・シン", "リサンドラ", "リリア", "リヴェン", "ルシアン", "ルブラン", "ルル", "レオナ", "レク＝サイ",
    "レナータ・グラスク", "レネクトン", "レル", "レンガー",
    "ワーウィック", "ヴァイ", "ヴァルス", "ヴィエゴ", "ヴェイン", "ヴェックス", "ヴェル＝コズ"
]


##English version of the champion list
##champion_list = [
    ##"Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Ambessa", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Aurora",
    ##"Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia",
    ##"Cho'Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal",
    ##"Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen",
    ##"Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce",
    ##"Jhin", "Jinx", "K'Sante", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
    ##"Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia",
    ##"Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Milio", "Miss Fortune",
    ##"Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne",
    ##"Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan",
    ##"Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira",
    ##"Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
    ##"Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric",
    ##"Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot",
    ##"Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear",
    ##"Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac",
    ##"Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
##]


champion_list.sort()


class DraftTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Fearless Draft Tool - BO5")

        self.remaining_champions = champion_list.copy()
        self.current_game = 0 
        self.blue_picks = [[] for _ in range(5)]
        self.red_picks = [[] for _ in range(5)]

        self.blue_listboxes = []
        self.red_listboxes = []

        self.selected = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.selected, values=self.remaining_champions, state="readonly", width=30)
        self.dropdown.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.blue_button = ttk.Button(root, text="Blue team picked", command=self.pick_blue)
        self.blue_button.grid(row=0, column=2, padx=5)

        self.red_button = ttk.Button(root, text="Red team picked", command=self.pick_red)
        self.red_button.grid(row=0, column=3, padx=5)

        self.next_button = ttk.Button(root, text="Next Game", command=self.next_game)
        self.next_button.grid(row=0, column=4, padx=10)

    
        ttk.Label(root, text="Blue").grid(row=1, column=0, columnspan=2)
        ttk.Label(root, text="Red").grid(row=1, column=2, columnspan=2)

        
        for game in range(5):
            row_num = game + 2
            ttk.Label(root, text=f"Game {game+1}").grid(row=row_num, column=0, pady=2)
            blue_box = tk.Listbox(root, height=5, width=30)
            blue_box.grid(row=row_num, column=1, padx=2, pady=2)
            self.blue_listboxes.append(blue_box)

            ttk.Label(root, text=f"Game {game+1}").grid(row=row_num, column=2, pady=2)
            red_box = tk.Listbox(root, height=5, width=30)
            red_box.grid(row=row_num, column=3, padx=2, pady=2)
            self.red_listboxes.append(red_box)

    def pick_blue(self):
        champ = self.selected.get()
        if champ in self.remaining_champions and self.current_game < 5:
            self.blue_picks[self.current_game].append(champ)
            self.remaining_champions.remove(champ)
            self.blue_listboxes[self.current_game].insert(tk.END, champ)
            self.update_dropdown()

    def pick_red(self):
        champ = self.selected.get()
        if champ in self.remaining_champions and self.current_game < 5:
            self.red_picks[self.current_game].append(champ)
            self.remaining_champions.remove(champ)
            self.red_listboxes[self.current_game].insert(tk.END, champ)
            self.update_dropdown()

    def next_game(self):
        if self.current_game < 4:
            self.current_game += 1
        else:
            self.next_button.config(state="disabled")  
        self.update_dropdown()

    def update_dropdown(self):
        self.dropdown['values'] = self.remaining_champions
        self.selected.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = DraftTool(root)
    root.mainloop()
