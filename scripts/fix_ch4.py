from pathlib import Path
R = Path(__file__).resolve().parent.parent
BS = chr(92)
def E(x): return BS + "textenglish{" + x + "}"
def MB(x): return BS + "mbox{" + E(x) + "}"
D = BS + "$"
p = R/"chapters/ch4-market.tex"; lines = p.read_text(encoding="utf-8").split("\n")
i = 23
assert lines[i].startswith("הפירוט הבא")
new = ("הפירוט הבא משלים את התמונה לפי מה שתועד בדפי המוצר ובבדיקת הצוות. "
 + E("LTX Studio") + ": " + MB("Lite "+D+"15, Standard "+D+"35, Pro "+D+"125") + ". דמויות שמורות זמינות רק מהמסלול " + E("Standard") + ", ולכן מחיר הכניסה ליכולת המרכזית גבוה ביותר מפי שניים ממחיר המסלול הזול. חולשתו בבדיקת הצוות היא שאי אפשר לנסות אותו בלי תשלום. "
 + E("OpenArt") + ": המסלול " + E("Starter") + " כולל כ־13 דמויות עקביות, והמסלול " + E("Wonder") + " כ־353. בבדיקת הצוות הטעינה התארכה ולא הופקה תוצאה. "
 + E("LongStories.ai") + ": " + MB("Pro "+D+"59, Creator "+D+"99, Creator Max "+D+"199") + ". מסלול חינמי קיים אך ללא וידאו, ולכן גם כאן לא ניתן היה לבדוק עברית. "
 + E("Atlabs") + ": " + MB("Lite "+D+"19, Pro "+D+"39, Plus "+D+"79, Max "+D+"249") + ", לפי דף המחירים של המוצר (צילום מסך של הצוות, 22.11.2026). שמירת דמויות עקביות מתחילה במסלול " + E("Pro") + " ואינה כלולה במסלול " + E("Lite") + "; תרגום ליותר מ־40 שפות מופיע רק במסלול " + E("Max") + ".")
lines[i] = new
j = 65
assert lines[j].startswith(BS + "‏") or lines[j].startswith("איור")
lines[j] = lines[j].rstrip() + " לגבי " + E("CapCut") + " מוצג מחיר המנוי היחיד שלו, שאינו כולל דמויות עקביות."
p.write_text("\n".join(lines), encoding="utf-8", newline="")
p = R/"chapters/ch1-intro.tex"; s = p.read_text(encoding="utf-8")
a = "אך אף מוצר אינו מציג תיעוד של"
assert a in s
s = s.replace(a, "אך באף אחד מהמוצרים שנבדקו לא נמצא תיעוד של")
a = E("Atlabs") + " מצהיר על תמיכה בעברית, בתוכניות בתשלום"
assert a in s
s = s.replace(a, E("Atlabs") + BS + "cite{atlabs}" .replace(BS+"cite", "~"+BS+"cite") + " מצהיר על תמיכה בעברית, בתוכניות בתשלום")
p.write_text(s, encoding="utf-8", newline="")
