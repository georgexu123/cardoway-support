from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EMAIL = "georgexu12345@163.com"

LANGUAGES = {
    "en-US": "English",
    "zh-Hans": "简体中文",
    "zh-Hant": "繁體中文",
    "ja-JP": "日本語",
    "ko-KR": "한국어",
    "de-DE": "Deutsch",
    "fr-FR": "Français",
    "ru-RU": "Русский",
}

COPY = {
    "en-US": {
        "html_lang": "en",
        "overview": "Overview", "support": "Support", "privacy": "Privacy",
        "home_eyebrow": "A CLASSIC DECK · A NEW JOURNEY",
        "home_title": "Turn a card. Follow the journey.",
        "home_lede": "A relaxed 52-card game for iPhone. Play with two to four travelers, collect matching cards, and enjoy the journey without a timer.",
        "features_title": "Simple rules, thoughtful choices",
        "features": [
            ("Relaxed mode", "Matching cards are collected automatically, so you can settle in and enjoy the rhythm of every turn."),
            ("Observation mode", "Spot the matching older card yourself. A careful eye makes every journey more rewarding."),
            ("Five complete themes", "Travel through vintage night, paper craft, neon, aurora, and lantern worlds with matching effects."),
        ],
        "privacy_teaser_title": "A calm game that stays on your device",
        "privacy_teaser": "Your journey, settings, and records are saved locally. Cardoway has no advertising or cross-app tracking.",
        "support_title": "How can we help?", "support_intro": "Cardoway supports iPhone models running iOS 17 or later.",
        "faqs": [
            ("How do I restore my full-version purchase?", "Open Settings in Cardoway, find the full-version panel, and choose Restore Purchases. Make sure the device is signed in with the Apple Account used for the original purchase and can connect to the App Store."),
            ("Where is my saved game?", "The current journey, preferences, and records are stored on this device. Cardoway resumes an unfinished game automatically. Deleting the app also deletes this local data."),
            ("What is the difference between the two play modes?", "Relaxed mode collects a matching sequence automatically. In Observation mode, you choose the older matching card yourself; choosing incorrectly or passing ends the turn."),
            ("Why is a theme locked?", "The included theme is ready to use. Four additional themes can be previewed before the one-time full-version purchase, which unlocks their matching artwork and effects."),
        ],
        "contact_title": "Still need help?", "contact_text": "Email us with your device model, iOS version, Cardoway version, what happened before the issue, and a screenshot when possible.",
        "privacy_title": "Your journey stays yours.", "effective": "Effective September 16, 2026",
        "privacy_intro": "Cardoway is an offline card game. The developer does not provide an account system, advertising, cross-app tracking, third-party analytics SDKs, or developer-operated servers that store player data.",
        "privacy_sections": [
            ("Data stored on your device", "Cardoway stores your current game, settings, play mode, theme choice, and game records locally on your device. This information is used only to provide the game’s features and is not uploaded to the developer. Deleting the app deletes this local data."),
            ("In-app purchases", "The full-version purchase and purchase restoration are processed by Apple through the App Store and StoreKit. The developer does not receive your payment credentials. Cardoway reads only the purchase entitlement information Apple makes available to the app."),
            ("Data collection and tracking", "Cardoway does not collect personal information, precise location, contacts, photos, microphone recordings, health data, advertising identifiers, or usage analytics. It does not track you across apps or websites."),
            ("Children", "Cardoway does not knowingly collect personal information from children or any other users."),
            ("Changes to this policy", "If Cardoway’s privacy practices change materially, this policy will be updated with the relevant app version and a new effective date."),
        ],
        "contact_privacy": "For privacy or support questions, email",
        "tagline": "A relaxed card journey for iPhone.", "read_privacy": "Read the privacy policy", "get_support": "Get support",
    },
    "zh-Hans": {
        "html_lang": "zh-Hans",
        "overview": "游戏介绍", "support": "技术支持", "privacy": "隐私政策",
        "home_eyebrow": "一副经典纸牌 · 一段全新旅程",
        "home_title": "翻开一张牌，继续这段旅程。",
        "home_lede": "一款轻松的 iPhone 纸牌游戏。2 至 4 位旅伴轮流翻牌、收起同点数牌，没有倒计时，慢慢来。",
        "features_title": "规则简单，每一步都值得留意",
        "features": [("轻松模式", "自动收起同点数牌，让你专注于每一轮自然流动的节奏。"), ("观察模式", "亲自找出较早出现的同点数牌，细心观察会让每段旅程更有趣。"), ("五套完整主题", "穿行于复古夜车、纸艺车站、星夜霓虹、极光雪国与东方灯会，每套都有专属画面和特效。")],
        "privacy_teaser_title": "安静游玩，数据留在设备上",
        "privacy_teaser": "旅程、设置与战绩保存在本机。Cardoway 不含广告，也不会跨 App 追踪。",
        "support_title": "需要什么帮助？", "support_intro": "Cardoway 支持运行 iOS 17 或更高版本的 iPhone。",
        "faqs": [("如何恢复完整版本购买？", "打开 Cardoway 的“设置”，找到完整版本区域并选择“恢复购买”。请确认设备登录的是购买时使用的 Apple 账户，并且可以连接 App Store。"), ("我的存档在哪里？", "当前旅程、偏好和战绩保存在这台设备上。Cardoway 会自动继续尚未完成的游戏。删除 App 也会删除这些本地数据。"), ("两种玩法有什么区别？", "轻松模式会自动收起相配的牌列；观察模式需要你亲自选择较早出现的同点数牌，选错或放弃都会结束本轮。"), ("为什么有些主题被锁定？", "随游戏提供的主题可直接使用。另外四套主题可以免费预览，一次买断完整版本后会解锁相应画面与特效。")],
        "contact_title": "仍然需要帮助？", "contact_text": "请在邮件中写明设备型号、iOS 版本、Cardoway 版本、问题发生前的操作，并尽可能附上截图。",
        "privacy_title": "你的旅程，只属于你。", "effective": "生效日期：2026 年 9 月 16 日",
        "privacy_intro": "Cardoway 是一款单机纸牌游戏。开发者不提供自有账号系统、广告、跨 App 追踪、第三方分析 SDK，也不运营用于保存玩家数据的服务器。",
        "privacy_sections": [("设备上的本地数据", "Cardoway 会在设备本地保存当前游戏、设置、玩法、主题选择和战绩。这些信息仅用于提供游戏功能，不会上传给开发者。删除 App 会删除这些本地数据。"), ("App 内购买", "完整版本购买与恢复购买由 Apple 通过 App Store 和 StoreKit 处理。开发者不会获得你的付款凭证；Cardoway 只读取 Apple 向 App 提供的购买权益状态。"), ("数据收集与追踪", "Cardoway 不收集个人信息、精确位置、通讯录、照片、麦克风录音、健康数据、广告标识符或使用情况分析，也不会跨 App 或网站追踪你。"), ("儿童", "Cardoway 不会有意收集儿童或其他用户的个人信息。"), ("政策变更", "如果 Cardoway 的隐私做法发生实质变化，本政策会随相关 App 版本更新，并注明新的生效日期。")],
        "contact_privacy": "隐私或支持问题请联系", "tagline": "一段轻松的 iPhone 纸牌旅程。", "read_privacy": "阅读隐私政策", "get_support": "获取帮助",
    },
    "zh-Hant": {
        "html_lang": "zh-Hant",
        "overview": "遊戲介紹", "support": "技術支援", "privacy": "隱私權政策",
        "home_eyebrow": "一副經典紙牌 · 一段全新旅程", "home_title": "翻開一張牌，繼續這段旅程。",
        "home_lede": "一款輕鬆的 iPhone 紙牌遊戲。2 至 4 位旅伴輪流翻牌、收起同點數牌，沒有倒數計時，慢慢來。",
        "features_title": "規則簡單，每一步都值得留意",
        "features": [("輕鬆模式", "自動收起同點數牌，讓你專注於每一輪自然流動的節奏。"), ("觀察模式", "親自找出較早出現的同點數牌，細心觀察會讓每段旅程更有趣。"), ("五套完整主題", "穿行於復古夜車、紙藝車站、星夜霓虹、極光雪國與東方燈會，每套都有專屬畫面和特效。")],
        "privacy_teaser_title": "安靜遊玩，資料留在裝置上", "privacy_teaser": "旅程、設定與戰績保存在本機。Cardoway 不含廣告，也不會跨 App 追蹤。",
        "support_title": "需要什麼協助？", "support_intro": "Cardoway 支援執行 iOS 17 或更新版本的 iPhone。",
        "faqs": [("如何恢復完整版本購買？", "開啟 Cardoway 的「設定」，找到完整版本區域並選擇「恢復購買」。請確認裝置登入的是購買時使用的 Apple 帳號，並且可以連接 App Store。"), ("我的存檔在哪裡？", "目前旅程、偏好和戰績保存在這部裝置上。Cardoway 會自動繼續尚未完成的遊戲。刪除 App 也會刪除這些本機資料。"), ("兩種玩法有什麼差別？", "輕鬆模式會自動收起相配的牌列；觀察模式需要你親自選擇較早出現的同點數牌，選錯或放棄都會結束本輪。"), ("為什麼有些主題被鎖定？", "隨遊戲提供的主題可直接使用。另外四套主題可以免費預覽，一次買斷完整版本後會解鎖相應畫面與特效。")],
        "contact_title": "仍然需要協助？", "contact_text": "請在郵件中寫明裝置型號、iOS 版本、Cardoway 版本、問題發生前的操作，並盡可能附上螢幕截圖。",
        "privacy_title": "你的旅程，只屬於你。", "effective": "生效日期：2026 年 9 月 16 日",
        "privacy_intro": "Cardoway 是一款單機紙牌遊戲。開發者不提供自有帳號系統、廣告、跨 App 追蹤、第三方分析 SDK，也不營運用於保存玩家資料的伺服器。",
        "privacy_sections": [("裝置上的本機資料", "Cardoway 會在裝置本機保存目前遊戲、設定、玩法、主題選擇和戰績。這些資訊僅用於提供遊戲功能，不會上傳給開發者。刪除 App 會刪除這些本機資料。"), ("App 內購買", "完整版本購買與恢復購買由 Apple 透過 App Store 和 StoreKit 處理。開發者不會取得你的付款憑證；Cardoway 只讀取 Apple 向 App 提供的購買權益狀態。"), ("資料收集與追蹤", "Cardoway 不收集個人資訊、精確位置、通訊錄、照片、麥克風錄音、健康資料、廣告識別碼或使用情況分析，也不會跨 App 或網站追蹤你。"), ("兒童", "Cardoway 不會有意收集兒童或其他使用者的個人資訊。"), ("政策變更", "如果 Cardoway 的隱私做法發生實質變化，本政策會隨相關 App 版本更新，並註明新的生效日期。")],
        "contact_privacy": "隱私或支援問題請聯絡", "tagline": "一段輕鬆的 iPhone 紙牌旅程。", "read_privacy": "閱讀隱私權政策", "get_support": "取得協助",
    },
    "ja-JP": {
        "html_lang": "ja",
        "overview": "ゲーム紹介", "support": "サポート", "privacy": "プライバシー",
        "home_eyebrow": "クラシックな一組 · 新しい旅", "home_title": "カードをめくり、旅を続けよう。",
        "home_lede": "iPhoneで楽しむ、ゆったりとした52枚のカードゲーム。2〜4人で順番にカードをめくり、同じ数字を集めます。時間制限はありません。",
        "features_title": "シンプルなルール、考える楽しさ",
        "features": [("リラックスモード", "同じ数字のカードを自動で集めます。毎ターンの心地よいリズムを楽しめます。"), ("観察モード", "同じ数字の古いカードを自分で見つけます。注意深く見るほど旅が楽しくなります。"), ("5つの完成テーマ", "夜行列車、ペーパークラフト、ネオン、オーロラ、灯籠の世界を専用エフェクトとともに旅します。")],
        "privacy_teaser_title": "データは端末の中に", "privacy_teaser": "旅の記録、設定、成績は端末内に保存されます。広告やアプリをまたぐトラッキングはありません。",
        "support_title": "お困りですか？", "support_intro": "CardowayはiOS 17以降を搭載したiPhoneに対応しています。",
        "faqs": [("フルバージョンの購入を復元するには？", "Cardowayの「設定」でフルバージョンの欄を開き、「購入を復元」を選択してください。購入時のApple Accountでサインインし、App Storeに接続できることをご確認ください。"), ("セーブデータはどこにありますか？", "進行中の旅、設定、成績はこの端末に保存されます。未完了のゲームは自動的に再開されます。Appを削除すると、このローカルデータも削除されます。"), ("2つのモードの違いは？", "リラックスモードでは同じ数字の並びを自動で集めます。観察モードでは古い同数字のカードを自分で選び、選択ミスやパスで手番が終了します。"), ("テーマがロックされているのはなぜ？", "付属テーマはすぐに使えます。追加の4テーマは無料で試着でき、フルバージョンを一度購入すると専用アートとエフェクトが解放されます。")],
        "contact_title": "解決しない場合", "contact_text": "端末の機種、iOSのバージョン、Cardowayのバージョン、問題が起きる前の操作、可能であればスクリーンショットを添えてメールしてください。",
        "privacy_title": "あなたの旅は、あなたのもの。", "effective": "施行日：2026年9月16日",
        "privacy_intro": "Cardowayはオフラインのカードゲームです。開発者独自のアカウント、広告、アプリをまたぐトラッキング、第三者分析SDK、プレイヤーデータを保存する開発者運営サーバーはありません。",
        "privacy_sections": [("端末に保存されるデータ", "進行中のゲーム、設定、プレイモード、テーマ、成績は端末内に保存されます。ゲーム機能のためだけに使用され、開発者へ送信されません。Appを削除するとローカルデータも削除されます。"), ("App内課金", "フルバージョンの購入と復元は、AppleがApp StoreとStoreKitを通じて処理します。開発者が支払い情報を受け取ることはありません。CardowayはAppleがAppに提供する購入権利の状態だけを読み取ります。"), ("データ収集とトラッキング", "個人情報、正確な位置情報、連絡先、写真、マイク録音、健康データ、広告識別子、利用状況分析を収集せず、AppやWebサイトをまたいで追跡しません。"), ("お子様", "Cardowayは、お子様を含む利用者の個人情報を意図的に収集しません。"), ("ポリシーの変更", "プライバシーの取り扱いに重要な変更がある場合は、該当するAppバージョンと新しい施行日を記載して本ポリシーを更新します。")],
        "contact_privacy": "プライバシーまたはサポートに関するお問い合わせ", "tagline": "iPhoneで楽しむ、ゆったりとしたカードの旅。", "read_privacy": "プライバシーポリシーを読む", "get_support": "サポートを見る",
    },
    "ko-KR": {
        "html_lang": "ko",
        "overview": "게임 소개", "support": "지원", "privacy": "개인정보 처리방침",
        "home_eyebrow": "클래식 카드 한 벌 · 새로운 여행", "home_title": "카드를 뒤집고, 여행을 이어가세요.",
        "home_lede": "iPhone에서 즐기는 편안한 52장 카드 게임입니다. 2~4명의 여행자가 차례로 카드를 뒤집고 같은 숫자를 모으며, 시간 제한 없이 천천히 즐길 수 있습니다.",
        "features_title": "간단한 규칙, 세심한 선택",
        "features": [("편안한 모드", "같은 숫자의 카드를 자동으로 모아 매 턴의 차분한 흐름을 즐길 수 있습니다."), ("관찰 모드", "먼저 놓인 같은 숫자의 카드를 직접 찾습니다. 주의 깊게 볼수록 여행이 더 재미있어집니다."), ("다섯 가지 완성형 테마", "빈티지 야간열차, 종이 공예, 네온, 오로라, 등불 세계를 전용 효과와 함께 여행하세요.")],
        "privacy_teaser_title": "조용한 게임, 기기에 남는 데이터", "privacy_teaser": "여행, 설정, 기록은 기기에 저장됩니다. Cardoway에는 광고나 앱 간 추적이 없습니다.",
        "support_title": "무엇을 도와드릴까요?", "support_intro": "Cardoway는 iOS 17 이상이 설치된 iPhone을 지원합니다.",
        "faqs": [("전체 버전 구매를 어떻게 복원하나요?", "Cardoway의 설정에서 전체 버전 영역을 열고 ‘구매 복원’을 선택하세요. 구입에 사용한 Apple 계정으로 로그인되어 있고 App Store에 연결할 수 있는지 확인하세요."), ("저장된 게임은 어디에 있나요?", "현재 여행, 환경설정, 기록은 이 기기에 저장됩니다. 끝나지 않은 게임은 자동으로 이어집니다. 앱을 삭제하면 이 로컬 데이터도 삭제됩니다."), ("두 플레이 모드는 무엇이 다른가요?", "편안한 모드에서는 같은 숫자의 카드 열을 자동으로 모읍니다. 관찰 모드에서는 먼저 놓인 같은 숫자의 카드를 직접 선택하며, 잘못 선택하거나 패스하면 턴이 끝납니다."), ("테마가 잠겨 있는 이유는 무엇인가요?", "기본 테마는 바로 사용할 수 있습니다. 추가 네 가지 테마는 무료로 미리 볼 수 있으며, 전체 버전을 한 번 구매하면 전용 아트와 효과가 잠금 해제됩니다.")],
        "contact_title": "도움이 더 필요한가요?", "contact_text": "기기 모델, iOS 버전, Cardoway 버전, 문제가 발생하기 전의 조작과 가능한 경우 스크린샷을 이메일로 보내 주세요.",
        "privacy_title": "당신의 여행은 당신의 것입니다.", "effective": "시행일: 2026년 9월 16일",
        "privacy_intro": "Cardoway는 오프라인 카드 게임입니다. 개발자 계정 시스템, 광고, 앱 간 추적, 타사 분석 SDK 또는 플레이어 데이터를 저장하는 개발자 운영 서버를 사용하지 않습니다.",
        "privacy_sections": [("기기에 저장되는 데이터", "현재 게임, 설정, 플레이 모드, 테마 선택, 게임 기록은 기기에 로컬로 저장됩니다. 이 정보는 게임 기능 제공에만 사용되며 개발자에게 전송되지 않습니다. 앱을 삭제하면 로컬 데이터도 삭제됩니다."), ("앱 내 구입", "전체 버전 구입과 복원은 Apple이 App Store와 StoreKit을 통해 처리합니다. 개발자는 결제 정보를 받지 않으며, Cardoway는 Apple이 앱에 제공하는 구입 권한 상태만 읽습니다."), ("데이터 수집 및 추적", "개인정보, 정확한 위치, 연락처, 사진, 마이크 녹음, 건강 데이터, 광고 식별자 또는 사용 분석을 수집하지 않으며 앱이나 웹사이트 간에 사용자를 추적하지 않습니다."), ("어린이", "Cardoway는 어린이를 포함한 사용자의 개인정보를 의도적으로 수집하지 않습니다."), ("정책 변경", "개인정보 처리 방식이 실질적으로 변경되면 관련 앱 버전과 새로운 시행일을 표시하여 이 정책을 업데이트합니다.")],
        "contact_privacy": "개인정보 또는 지원 문의", "tagline": "iPhone에서 즐기는 편안한 카드 여행.", "read_privacy": "개인정보 처리방침 보기", "get_support": "지원 받기",
    },
    "de-DE": {
        "html_lang": "de",
        "overview": "Übersicht", "support": "Support", "privacy": "Datenschutz",
        "home_eyebrow": "EIN KLASSISCHES BLATT · EINE NEUE REISE", "home_title": "Eine Karte aufdecken. Der Reise folgen.",
        "home_lede": "Ein entspanntes Kartenspiel mit 52 Karten für das iPhone. Zwei bis vier Reisende decken reihum Karten auf und sammeln gleiche Werte – ganz ohne Zeitdruck.",
        "features_title": "Einfache Regeln, überlegte Entscheidungen",
        "features": [("Entspannter Modus", "Passende Karten werden automatisch eingesammelt, damit du den ruhigen Rhythmus jeder Runde genießen kannst."), ("Beobachtungsmodus", "Finde die ältere Karte mit demselben Wert selbst. Ein gutes Auge macht jede Reise lohnender."), ("Fünf vollständige Themen", "Reise mit passenden Effekten durch Nachtzug-, Papierkunst-, Neon-, Polarlicht- und Laternenwelten.")],
        "privacy_teaser_title": "Ein ruhiges Spiel, das auf deinem Gerät bleibt", "privacy_teaser": "Reise, Einstellungen und Statistiken werden lokal gespeichert. Cardoway enthält keine Werbung und kein App-übergreifendes Tracking.",
        "support_title": "Wie können wir helfen?", "support_intro": "Cardoway unterstützt iPhones mit iOS 17 oder neuer.",
        "faqs": [("Wie stelle ich meinen Kauf der Vollversion wieder her?", "Öffne die Einstellungen in Cardoway, gehe zum Bereich Vollversion und wähle „Käufe wiederherstellen“. Das Gerät muss mit dem Apple Account des ursprünglichen Kaufs angemeldet sein und den App Store erreichen können."), ("Wo ist mein Spielstand?", "Die aktuelle Reise, Einstellungen und Statistiken werden auf diesem Gerät gespeichert. Eine nicht beendete Partie wird automatisch fortgesetzt. Beim Löschen der App werden auch diese lokalen Daten gelöscht."), ("Wie unterscheiden sich die beiden Spielmodi?", "Im entspannten Modus wird eine passende Kartenfolge automatisch eingesammelt. Im Beobachtungsmodus wählst du die ältere passende Karte selbst; eine falsche Wahl oder Passen beendet den Zug."), ("Warum ist ein Thema gesperrt?", "Das enthaltene Thema ist sofort verfügbar. Vier weitere Themen können vor dem einmaligen Kauf der Vollversion ausprobiert werden; danach werden ihre Grafiken und Effekte freigeschaltet.")],
        "contact_title": "Noch Hilfe nötig?", "contact_text": "Schreib uns dein Gerätemodell, die iOS- und Cardoway-Version, die Schritte vor dem Problem und füge möglichst einen Screenshot bei.",
        "privacy_title": "Deine Reise bleibt deine.", "effective": "Gültig ab 16. September 2026",
        "privacy_intro": "Cardoway ist ein Offline-Kartenspiel. Der Entwickler bietet kein eigenes Kontosystem, keine Werbung, kein App-übergreifendes Tracking, keine Analyse-SDKs Dritter und keine eigenen Server zur Speicherung von Spielerdaten.",
        "privacy_sections": [("Daten auf deinem Gerät", "Aktuelle Partie, Einstellungen, Spielmodus, Themenwahl und Statistiken werden lokal auf deinem Gerät gespeichert. Sie dienen nur den Spielfunktionen und werden nicht an den Entwickler übertragen. Beim Löschen der App werden diese Daten gelöscht."), ("In-App-Käufe", "Kauf und Wiederherstellung der Vollversion werden von Apple über App Store und StoreKit verarbeitet. Der Entwickler erhält keine Zahlungsdaten. Cardoway liest nur den von Apple bereitgestellten Kaufstatus."), ("Datenerhebung und Tracking", "Cardoway erhebt keine personenbezogenen Daten, genauen Standorte, Kontakte, Fotos, Mikrofonaufnahmen, Gesundheitsdaten, Werbe-IDs oder Nutzungsanalysen und verfolgt dich nicht über Apps oder Websites hinweg."), ("Kinder", "Cardoway erhebt wissentlich keine personenbezogenen Daten von Kindern oder anderen Nutzern."), ("Änderungen", "Bei wesentlichen Änderungen der Datenschutzpraxis wird diese Richtlinie mit der entsprechenden App-Version und einem neuen Gültigkeitsdatum aktualisiert.")],
        "contact_privacy": "Bei Fragen zu Datenschutz oder Support schreibe an", "tagline": "Eine entspannte Kartenreise fürs iPhone.", "read_privacy": "Datenschutzrichtlinie lesen", "get_support": "Support erhalten",
    },
    "fr-FR": {
        "html_lang": "fr",
        "overview": "Aperçu", "support": "Assistance", "privacy": "Confidentialité",
        "home_eyebrow": "UN JEU CLASSIQUE · UN NOUVEAU VOYAGE", "home_title": "Retournez une carte. Suivez le voyage.",
        "home_lede": "Un jeu de 52 cartes paisible pour iPhone. Deux à quatre voyageurs retournent les cartes à tour de rôle et réunissent les mêmes valeurs, sans chrono.",
        "features_title": "Des règles simples, des choix attentifs",
        "features": [("Mode Détente", "Les cartes de même valeur sont ramassées automatiquement, pour profiter du rythme de chaque tour."), ("Mode Observation", "Repérez vous-même l’ancienne carte de même valeur. Chaque détail compte."), ("Cinq thèmes complets", "Voyagez entre train de nuit, papier découpé, néons, aurores et lanternes, avec leurs effets assortis.")],
        "privacy_teaser_title": "Un jeu calme qui reste sur votre appareil", "privacy_teaser": "Votre voyage, vos réglages et vos statistiques sont enregistrés localement. Cardoway ne contient ni publicité ni suivi entre apps.",
        "support_title": "Comment pouvons-nous vous aider ?", "support_intro": "Cardoway est compatible avec les iPhone sous iOS 17 ou version ultérieure.",
        "faqs": [("Comment restaurer mon achat de la version complète ?", "Ouvrez Réglages dans Cardoway, trouvez la section de la version complète et choisissez « Restaurer les achats ». Vérifiez que l’appareil utilise le compte Apple de l’achat initial et peut accéder à l’App Store."), ("Où est ma sauvegarde ?", "Le voyage en cours, les préférences et les statistiques sont enregistrés sur cet appareil. Cardoway reprend automatiquement une partie inachevée. Supprimer l’app efface aussi ces données locales."), ("Quelle différence entre les deux modes ?", "Le mode Détente ramasse automatiquement une suite correspondante. En mode Observation, vous choisissez l’ancienne carte de même valeur ; une erreur ou un passage termine le tour."), ("Pourquoi un thème est-il verrouillé ?", "Le thème inclus est disponible immédiatement. Quatre thèmes supplémentaires peuvent être essayés avant l’achat unique de la version complète, qui débloque leurs illustrations et effets.")],
        "contact_title": "Besoin d’aide supplémentaire ?", "contact_text": "Indiquez par e-mail le modèle de l’appareil, les versions d’iOS et de Cardoway, les étapes précédant le problème et, si possible, une capture d’écran.",
        "privacy_title": "Votre voyage reste le vôtre.", "effective": "Date d’entrée en vigueur : 16 septembre 2026",
        "privacy_intro": "Cardoway est un jeu de cartes hors ligne. Le développeur ne fournit ni compte propre, ni publicité, ni suivi entre apps, ni SDK d’analyse tiers, ni serveur exploitant les données des joueurs.",
        "privacy_sections": [("Données stockées sur votre appareil", "La partie en cours, les réglages, le mode, le thème et les statistiques sont enregistrés localement. Ces informations servent uniquement aux fonctions du jeu et ne sont pas envoyées au développeur. Supprimer l’app efface ces données."), ("Achats intégrés", "L’achat et la restauration de la version complète sont traités par Apple via l’App Store et StoreKit. Le développeur ne reçoit pas vos données de paiement. Cardoway lit uniquement l’état du droit d’achat fourni par Apple."), ("Collecte de données et suivi", "Cardoway ne collecte ni informations personnelles, ni localisation précise, contacts, photos, enregistrements du micro, données de santé, identifiants publicitaires ou analyses d’utilisation, et ne vous suit pas entre apps ou sites."), ("Enfants", "Cardoway ne collecte sciemment aucune information personnelle auprès des enfants ou d’autres utilisateurs."), ("Modifications", "Si les pratiques de confidentialité changent sensiblement, cette politique sera mise à jour avec la version concernée et une nouvelle date d’entrée en vigueur.")],
        "contact_privacy": "Pour toute question de confidentialité ou d’assistance, écrivez à", "tagline": "Un voyage de cartes paisible sur iPhone.", "read_privacy": "Lire la politique de confidentialité", "get_support": "Obtenir de l’aide",
    },
    "ru-RU": {
        "html_lang": "ru",
        "overview": "Об игре", "support": "Поддержка", "privacy": "Конфиденциальность",
        "home_eyebrow": "КЛАССИЧЕСКАЯ КОЛОДА · НОВОЕ ПУТЕШЕСТВИЕ", "home_title": "Откройте карту. Продолжайте путь.",
        "home_lede": "Спокойная игра с колодой из 52 карт для iPhone. От двух до четырёх путешественников по очереди открывают карты и собирают совпадающие значения — без таймера и спешки.",
        "features_title": "Простые правила, вдумчивые решения",
        "features": [("Спокойный режим", "Совпадающие карты собираются автоматически, чтобы вы могли наслаждаться ритмом каждого хода."), ("Режим наблюдения", "Самостоятельно найдите более раннюю карту того же значения. Внимательность делает путешествие интереснее."), ("Пять полных тем", "Путешествуйте по мирам ночного поезда, бумажной станции, неона, северного сияния и фонарей с особыми эффектами.")],
        "privacy_teaser_title": "Спокойная игра, данные остаются на устройстве", "privacy_teaser": "Путешествие, настройки и статистика хранятся локально. В Cardoway нет рекламы и межпрограммного отслеживания.",
        "support_title": "Чем мы можем помочь?", "support_intro": "Cardoway поддерживает iPhone с iOS 17 и новее.",
        "faqs": [("Как восстановить покупку полной версии?", "Откройте настройки Cardoway, найдите раздел полной версии и выберите «Восстановить покупки». Убедитесь, что на устройстве выполнен вход в Apple Account, использованный при покупке, и доступен App Store."), ("Где хранится сохранённая игра?", "Текущее путешествие, настройки и статистика хранятся на этом устройстве. Cardoway автоматически продолжает незавершённую игру. При удалении приложения локальные данные также удаляются."), ("Чем отличаются два режима?", "В спокойном режиме совпадающая последовательность собирается автоматически. В режиме наблюдения вы сами выбираете более раннюю карту того же значения; ошибка или пропуск завершает ход."), ("Почему тема заблокирована?", "Включённая тема доступна сразу. Ещё четыре темы можно посмотреть до разовой покупки полной версии, которая открывает соответствующие изображения и эффекты.")],
        "contact_title": "Нужна дополнительная помощь?", "contact_text": "Напишите модель устройства, версии iOS и Cardoway, действия перед возникновением проблемы и по возможности приложите снимок экрана.",
        "privacy_title": "Ваше путешествие остаётся вашим.", "effective": "Дата вступления в силу: 16 сентября 2026 г.",
        "privacy_intro": "Cardoway — офлайн-игра в карты. Разработчик не предоставляет собственную систему аккаунтов, рекламу, межпрограммное отслеживание, сторонние SDK аналитики или серверы для хранения данных игроков.",
        "privacy_sections": [("Данные на устройстве", "Текущая игра, настройки, режим, выбранная тема и статистика хранятся локально на устройстве. Они используются только для функций игры и не отправляются разработчику. Удаление приложения удаляет эти данные."), ("Встроенные покупки", "Покупка и восстановление полной версии обрабатываются Apple через App Store и StoreKit. Разработчик не получает платёжные данные. Cardoway читает только предоставленный Apple статус права на покупку."), ("Сбор данных и отслеживание", "Cardoway не собирает личные данные, точную геопозицию, контакты, фотографии, записи микрофона, данные о здоровье, рекламные идентификаторы или аналитику использования и не отслеживает вас между приложениями или сайтами."), ("Дети", "Cardoway намеренно не собирает личные данные детей или других пользователей."), ("Изменения", "При существенном изменении практик конфиденциальности политика будет обновлена с указанием соответствующей версии приложения и новой даты вступления в силу.")],
        "contact_privacy": "По вопросам конфиденциальности или поддержки пишите на", "tagline": "Спокойное карточное путешествие для iPhone.", "read_privacy": "Политика конфиденциальности", "get_support": "Получить помощь",
    },
}


def language_nav(locale: str, page: str) -> str:
    links = []
    for code, label in LANGUAGES.items():
        current = ' aria-current="true"' if code == locale else ""
        links.append(f'<a lang="{code}" hreflang="{code}" href="../{code}/{page}"{current}>{escape(label)}</a>')
    return '<nav class="locale-nav" aria-label="Languages">' + "".join(links) + "</nav>"


def header(locale: str, page: str) -> str:
    c = COPY[locale]
    links = []
    for filename, key in (("index.html", "overview"), ("support.html", "support"), ("privacy.html", "privacy")):
        current = ' aria-current="page"' if filename == page else ""
        links.append(f'<a href="{filename}"{current}>{escape(c[key])}</a>')
    return f'''<header class="site-header"><a class="brand" href="index.html" aria-label="Cardoway"><img src="../assets/app-icon.png" alt="" width="44" height="44"><span>Cardoway</span></a><nav aria-label="Primary navigation">{"".join(links)}</nav></header>'''


def footer(locale: str, page: str) -> str:
    c = COPY[locale]
    return f'''{language_nav(locale, page)}<footer><div><strong>Cardoway</strong><span>{escape(c["tagline"])}</span></div><div class="footer-links"><a href="mailto:{EMAIL}">{escape(c["support"])}</a><a href="privacy.html">{escape(c["privacy"])}</a></div><p>© 2026 George Xu</p></footer>'''


def head(locale: str, title: str, description: str) -> str:
    return f'''<!doctype html><html lang="{COPY[locale]["html_lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#092f29"><meta name="description" content="{escape(description, quote=True)}"><title>{escape(title)}</title><link rel="icon" type="image/png" href="../assets/app-icon.png"><link rel="stylesheet" href="../styles.css"></head><body>'''


def home_page(locale: str) -> str:
    c = COPY[locale]
    features = "".join(f'<article><span class="number">0{i}</span><h3>{escape(title)}</h3><p>{escape(text)}</p></article>' for i, (title, text) in enumerate(c["features"], 1))
    return head(locale, f'Cardoway — {c["tagline"]}', c["home_lede"]) + header(locale, "index.html") + f'''
<main><section class="hero"><div class="hero-copy"><p class="eyebrow">{escape(c["home_eyebrow"])}</p><h1>{escape(c["home_title"])}</h1><p class="lede">{escape(c["home_lede"])}</p><div class="hero-actions"><a class="button primary" href="support.html">{escape(c["get_support"])}</a><a class="button secondary" href="#features">{escape(c["overview"])}</a></div></div><div class="hero-art"><img class="game-shot" src="../assets/gameplay.jpg" alt="Cardoway"><img class="app-icon" src="../assets/app-icon.png" alt="Cardoway"></div></section>
<section class="features" id="features"><div class="section-heading"><p class="eyebrow">CARDOWAY</p><h2>{escape(c["features_title"])}</h2></div><div class="feature-grid">{features}</div></section>
<section class="quiet-card"><p class="eyebrow">PRIVACY</p><h2>{escape(c["privacy_teaser_title"])}</h2><p>{escape(c["privacy_teaser"])}</p><a href="privacy.html">{escape(c["read_privacy"])} <span aria-hidden="true">→</span></a></section></main>''' + footer(locale, "index.html") + "</body></html>"


def support_page(locale: str) -> str:
    c = COPY[locale]
    faqs = "".join(f'<section><h2>{escape(question)}</h2><p>{escape(answer)}</p></section>' for question, answer in c["faqs"])
    return head(locale, f'{c["support"]} — Cardoway', c["support_intro"]) + header(locale, "support.html") + f'''
<main class="document-shell"><header class="document-title"><p class="eyebrow">CARDOWAY SUPPORT</p><h1>{escape(c["support_title"])}</h1><p>{escape(c["support_intro"])}</p></header><article class="document-card">{faqs}<section class="contact-panel"><p class="eyebrow">CONTACT</p><h2>{escape(c["contact_title"])}</h2><p>{escape(c["contact_text"])}</p><a class="button primary" href="mailto:{EMAIL}">{EMAIL}</a></section></article></main>''' + footer(locale, "support.html") + "</body></html>"


def privacy_page(locale: str) -> str:
    c = COPY[locale]
    sections = "".join(f'<section><h2>{escape(title)}</h2><p>{escape(text)}</p></section>' for title, text in c["privacy_sections"])
    return head(locale, f'{c["privacy"]} — Cardoway', c["privacy_intro"]) + header(locale, "privacy.html") + f'''
<main class="document-shell"><header class="document-title"><p class="eyebrow">PRIVACY POLICY</p><h1>{escape(c["privacy_title"])}</h1><p>{escape(c["effective"])}</p></header><article class="document-card privacy-copy"><p>{escape(c["privacy_intro"])}</p>{sections}<section><h2>{escape(c["support"])}</h2><p>{escape(c["contact_privacy"])} <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></section></article></main>''' + footer(locale, "privacy.html") + "</body></html>"


for locale in LANGUAGES:
    directory = ROOT / locale
    directory.mkdir(exist_ok=True)
    (directory / "index.html").write_text(home_page(locale), encoding="utf-8")
    (directory / "support.html").write_text(support_page(locale), encoding="utf-8")
    (directory / "privacy.html").write_text(privacy_page(locale), encoding="utf-8")
