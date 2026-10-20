"""Builds index.html (EN) and es/index.html (ES) from one template.

Run from the repo root:  python tools/build.py
"""
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
PHONE = "18632669575"
FACEBOOK = "https://www.facebook.com/LaPatronaTrailersOFICIAL/"
MAPS = "https://www.google.com/maps/search/?api=1&query=" + quote("2900 Titan Row, Suite 130, Orlando, FL 32817")

ICONS = {
    "arrow": '<path d="M7 17 17 7M8.5 7H17v8.5"/>',
    "left": '<path d="M19 12H5m6-6-6 6 6 6"/>',
    "right": '<path d="M5 12h14m-6-6 6 6-6 6"/>',
    "up": '<path d="M12 19V5m-6 6 6-6 6 6"/>',
    "chat": '<path d="M20.5 11.6a8.4 8.4 0 0 1-12.3 7.5L3.5 20.5l1.4-4.6A8.4 8.4 0 1 1 20.5 11.6Z"/><path d="M9 9.2c.2 1.9 1.9 4.4 4.6 5.3l1.2-1.2 1.7.8-.4 1.6c-3.6.4-7.4-3.1-7.9-6.6l1.5-.6.9 1.6Z"/>',
    "person": '<circle cx="12" cy="7" r="3.6"/><path d="M4.5 21a7.5 7.5 0 0 1 15 0Z"/>',
    "phone": '<path d="M5 3.5h3.2l1.6 4.4-2.2 1.4a11.5 11.5 0 0 0 5.6 5.6l1.4-2.2 4.4 1.6V19a1.8 1.8 0 0 1-1.9 1.8A16.5 16.5 0 0 1 3.2 5.4 1.8 1.8 0 0 1 5 3.5Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    "fb": '<path d="M14 21v-7.5h2.6l.4-3H14V8.6c0-.9.3-1.5 1.6-1.5H17V4.4a20 20 0 0 0-2.3-.1c-2.3 0-3.8 1.4-3.8 3.9v2.3H8.3v3H11V21"/>',
}


def icon(name, cls="icon", filled=False):
    paint = 'fill="currentColor" stroke="none"' if filled else 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg class="{cls}" viewBox="0 0 24 24" {paint} aria-hidden="true">{ICONS[name]}</svg>'


def wa(text):
    return f"https://wa.me/{PHONE}?text={quote(text)}"


REVIEWS = [  # verbatim from the client's Facebook recommendations (screenshots on the live site)
    ("Canee Obafial", {"en": "June 28", "es": "28 de junio"}, "en",
     "Thank you La Patrona Trailers for my first food truck! We loved working with Nathaly, Clau and Edwin. They are experienced in making food trucks and we definitely recommend!"),
    ("Yunaisa Ramirez", {"en": "June 29", "es": "29 de junio"}, "es",
     "Excelente trabajo y atención. Te sugiero que consideres LA PATRONA Es un lugar genial para emprender tu proyecto de trabajo el equipo es muy profesional y el ambiente es muy agradable. También ofrecen buenas oportunidades para crecer con tu propia compañía."),
]

SIZES = [  # (key, length ft, crew min, crew max)
    ("8x10", 10, 1, 2),
    ("8x12", 12, 2, 2),
    ("8x14", 14, 2, 3),
    ("8x16", 16, 3, 4),
    ("8x20", 20, 4, 5),
]

T = {
    "en": {
        "lang": "en", "base": "", "other": "es/",
        "title": "La Patrona Trailers | Custom Food Trailers in Orlando, FL",
        "desc": "Customizable food trailers from 8×10 to 8×20 ft, designed and built in Orlando, Florida. Visit our facility and watch your trailer being built.",
        "skip": "Skip to content",
        "nav": ["Trailers", "Custom", "About", "Our work", "Founder"],
        "contact": "Contact", "quote": "Get a quote", "call": "Call La Patrona",
        "quote_url": "https://wa.link/mzfoe2",
        "hero_words": ("Food", "Trailers"),
        "hero_l1": "Customizable food trailers, built in Orlando.",
        "hero_l2": "Quality and personalization are our priorities. Visit our facility and watch your trailer being built.",
        "scroll": "Sizes 8×10 to 8×20 ft",
        "offer_h": "What we <em>offer</em>",
        "offer_p": "Explore our diverse range of customizable food trailers designed to meet the needs of every culinary entrepreneur. Quality and personalization are our priorities.",
        "tabs_label": "Trailer sizes", "custom_tab": "Custom",
        "ft": "ft", "dims": "Dimensions", "crew": "Capacity", "length": "length",
        "people": "people", "quote_size": "Quote the {s}",
        "wa_size": "Hi! I'd like a quote for the {s} ft food trailer.",
        "sizes": {
            "8x10": ("Perfect for first-time entrepreneurs.", "Compact and easy to move, ideal for coffee, juices, snacks, or fast food in small spaces.", "1–2 people working comfortably"),
            "8x12": ("Versatile and functional.", "Provides extra room for equipment and storage while staying highly mobile. A great choice for businesses at fairs, plazas, or food courts.", "2 people operating"),
            "8x14": ("The sweet spot between size and efficiency.", "Enough space to set up a complete basic kitchen (grill, fryer, refrigerator). Perfect for fast food, ice cream shops, or mobile bakeries.", "2–3 people"),
            "8x16": ("Spacious and built for growing businesses.", "Accommodates multiple industrial appliances and higher customer flow. Recommended for those looking to professionalize their operations and serve larger events.", "3–4 people"),
            "8x20": ("Designed for established businesses.", "Generous space, extra storage, and steady customer flow. Perfect for mobile restaurants, pizzerias, or kitchens with diverse menus.", "4–5 people"),
        },
        "custom_h": "Your vision, <em>our creation.</em>",
        "custom_p": "At La Patrona, we design and build custom food trucks tailored to your needs, including size, branding, kitchen, and other requirements. Share your idea with us, and we’ll create a unique food truck that represents your business and becomes a customer magnet.",
        "custom_btn": "Design yours",
        "wa_custom": "Hi! I'd like a quote for a personalized food trailer.",
        "custom_alt": "Personalized orange food trailer built by La Patrona",
        "about_h": "La Patrona Trailers is a leading provider of high-quality, customizable food trailers designed to empower mobile culinary entrepreneurs.",
        "about_p1": "Founded at the beginning of the year and quickly becoming a top seller in Florida, we specialize in crafting food trailers that combine durability, functionality, and style.",
        "about_p2": "Our mission is to bring your culinary vision to life with trailers built to meet your specific business needs. Whether you’re starting a food trailer business or expanding your fleet, our experienced team is here to guide you every step of the way.",
        "apart_h": "What sets us apart",
        "apart": [
            ("Transparency", "Customers are welcome to visit our facilities and see how their trailer is being built."),
            ("Customized support", "Customers help design their trailer layout to fit their exact needs."),
            ("Fair prices", "Competitive prices and uncompromising quality."),
        ],
        "visit_t": "Come see your trailer being built.",
        "directions": "Get directions",
        "work_h": "Our recent <em>work</em>",
        "work_p": "Take a look at our latest projects and see how we bring culinary visions to life with our customizable food trucks.",
        "prev": "Previous", "next": "Next", "delivered": "Delivered build",
        "work_alts": ["Customers with their black La Patrona food trailer", "Customers receiving their black food trailer", "La Patrona food trailers collage", "Hand holding La Patrona keychain in front of a new trailer"],
        "rev_h": "What our customers <em>say</em>",
        "rev_p": "Recommendations left by La Patrona customers on Facebook, shown as written.",
        "rev_meta": "Recommends La Patrona Trailers · Facebook · {date}",
        "finance": "Financing up to $30K",
        "rev_btn": "See more on Facebook",
        "rev_alts": ["Customer review on Facebook", "Customer review on Facebook"],
        "founder_role": "CEO, La Patrona Trailers",
        "founder_h": "About me: Nathaly, <em>CEO of La Patrona Trailers</em>",
        "founder_alt": "Nathaly Lastra, founder and CEO of La Patrona Trailers",
        "founder_ps": [
            "I’m Nathaly, founder and CEO of La Patrona Trailers, and my passion is helping entrepreneurs turn their dreams into reality. I’ve spent years in the food industry, gaining a deep understanding of the U.S. market, and I’ve channeled that knowledge to create a company that represents quality, innovation, and trust.",
            "For me, understanding each client’s unique needs is the key to creating customized solutions that really work. From the moment we start designing a trailer to the moment it hits the road, my team and I are committed to delivering more than just a trailer. We provide a strategic tool for your business success.",
            "At La Patrona Trailers, we don’t just build food trucks, we empower entrepreneurs. I believe that every business has a story to tell, and my goal is to give you the tools to write your own success story. My vision is to help people take that first step toward independence and financial freedom by equipping them with the best mobile kitchens.",
        ],
        "quote_text": "Investing in a food truck isn’t just about buying a vehicle; it’s about building a bridge to your financial freedom and entrepreneurial dreams. At La Patrona Trailers, we don’t just sell trailers, we create opportunities.",
        "quote_foot": "A personal reflection, Nathaly Lastra",
        "cta_h": "Let’s build your <em>food trailer.</em>",
        "cta_btn": "Get a quote on WhatsApp",
        "contact_h": "Contact <em>La Patrona Trailers</em>",
        "contact_p": "Leave us your details and Lastra Multiservice LLC will contact you.",
        "f": {"first": "First name", "last": "Last name", "phone": "Phone", "email": "Email", "city": "City"},
        "sms": "I agree to receive SMS messages from La Patrona Trailers related to my appointment, including confirmations, reminders, and follow-ups. Messages will be sent up to a maximum of 4 per appointment, and message and data rates may apply. Reply STOP to cancel at any time. Messages will be sent as often as necessary to keep me informed about my appointment, which may include important reminders and updates before and after the appointment.",
        "accept": "I have read and accept the", "terms": "Terms and Conditions", "privacy_l": "Privacy Policy",
        "send": "Send contact request",
        "form_note": "In this preview, sending opens WhatsApp with your details.",
        "err_req": "Required.", "err_email": "Enter a valid email.", "err_sum": "Please complete the highlighted fields.",
        "ok": "Opening WhatsApp with your details…",
        "wa_form": "Hi! I'd like La Patrona Trailers to contact me.",
        "policies_h": "Policies", "schedule_h": "Schedule", "contact_h2": "Contact",
        "legal": [
            ("Privacy Policy", "privacy-policy-2/"), ("Terms and conditions of use", "terms-and-conditions/"),
            ("SMS Policy", "sms-messaging-policy/"), ("Cookie Policy", "cookie-policy/"),
            ("Legal Notice", "legal-notice/"), ("Terms of Service", "terms-of-service/"),
        ],
        "legal_base": "https://www.lapatronatrailers.com/en/",
        "hours": [("Monday – Friday", "11:00 AM – 3:00 PM · 4:30 PM – 10:00 PM"), ("Saturday – Sunday", "4:30 PM – 10:00 PM")],
        "to_top": "Back to top",
        "logo_alt": "La Patrona Trailers home",
    },
    "es": {
        "lang": "es", "base": "../", "other": "../",
        "title": "La Patrona Trailers | Food trailers personalizados en Orlando, FL",
        "desc": "Remolques de comida personalizables de 8×10 a 8×20 pies, diseñados y construidos en Orlando, Florida. Visita nuestras instalaciones y mira cómo se construye tu trailer.",
        "skip": "Ir al contenido",
        "nav": ["Trailers", "Personalizado", "Nosotros", "Trabajos", "Fundadora"],
        "contact": "Contacto", "quote": "Cotizar", "call": "Llamar a La Patrona",
        "quote_url": wa("¡Hola! Quisiera recibir más información sobre los food trailers."),
        "hero_words": ("Food", "Trailers"),
        "hero_l1": "Food trailers personalizados, construidos en Orlando.",
        "hero_l2": "La calidad y la personalización son nuestras prioridades. Visita nuestras instalaciones y mira cómo se construye tu trailer.",
        "scroll": "Tamaños de 8×10 a 8×20 pies",
        "offer_h": "Lo que <em>ofrecemos</em>",
        "offer_p": "Explora nuestra diversa gama de remolques de comida personalizables, diseñados para satisfacer las necesidades de cada emprendedor culinario. La calidad y la personalización son nuestras prioridades.",
        "tabs_label": "Tamaños de trailer", "custom_tab": "Personalizado",
        "ft": "pies", "dims": "Medidas", "crew": "Capacidad", "length": "de largo",
        "people": "personas", "quote_size": "Cotizar el {s}",
        "wa_size": "¡Hola! Quisiera una cotización del food trailer de {s} pies.",
        "sizes": {
            "8x10": ("Perfecto para emprendedores primerizos.", "Compacto y fácil de mover, ideal para café, jugos, refrigerios o comida rápida en espacios reducidos.", "1 o 2 personas trabajando cómodamente"),
            "8x12": ("Versátil y funcional.", "Ofrece espacio adicional para equipos y almacenamiento, manteniendo al mismo tiempo una gran movilidad. Una excelente opción para negocios en ferias, plazas o patios de comidas.", "2 personas operando"),
            "8x14": ("El punto ideal entre tamaño y eficiencia.", "Espacio suficiente para montar una cocina básica completa (plancha, freidora, refrigerador). Perfecto para comida rápida, heladerías o panaderías móviles.", "2–3 personas"),
            "8x16": ("Espacioso y diseñado para empresas en crecimiento.", "Tiene capacidad para múltiples electrodomésticos industriales y un mayor flujo de clientes. Recomendado para quienes buscan profesionalizar sus operaciones y atender eventos de mayor envergadura.", "3–4 personas"),
            "8x20": ("Diseñado para negocios consolidados.", "Amplio espacio, almacenamiento adicional y flujo constante de clientes. Perfecto para restaurantes móviles, pizzerías o cocinas con menús variados.", "4–5 personas"),
        },
        "custom_h": "Tu visión, <em>nuestra creación.</em>",
        "custom_p": "En La Patrona diseñamos y construimos food trucks personalizados, adaptados a tus necesidades, incluyendo tamaño, marca, cocina y otros requisitos. Comparte tu idea con nosotros y crearemos un food truck único que represente tu negocio y se convierta en un imán para clientes.",
        "custom_btn": "Diseña el tuyo",
        "wa_custom": "¡Hola! Quisiera una cotización de un food trailer personalizado.",
        "custom_alt": "Food trailer naranja personalizado construido por La Patrona",
        "about_h": "La Patrona Trailers es un proveedor líder de remolques de comida personalizables de alta calidad, diseñados para impulsar a emprendedores culinarios móviles.",
        "about_p1": "Fundada a principios de año y consolidándose rápidamente como un éxito de ventas en Florida, nos especializamos en la fabricación de remolques de comida que combinan durabilidad, funcionalidad y estilo.",
        "about_p2": "Nuestra misión es hacer realidad su visión culinaria con remolques diseñados para satisfacer las necesidades específicas de su negocio. Ya sea que esté iniciando un negocio de remolques de comida o ampliando su flota, nuestro equipo de expertos está aquí para guiarlo en cada paso del proceso.",
        "apart_h": "Lo que nos distingue",
        "apart": [
            ("Transparencia", "Los clientes son bienvenidos a visitar nuestras instalaciones y ver cómo se construye su remolque."),
            ("Soporte personalizado", "Los clientes ayudan a diseñar la distribución de su remolque para que se ajuste a sus necesidades exactas."),
            ("Precios justos", "Precios competitivos y calidad sin concesiones."),
        ],
        "visit_t": "Ven a ver cómo se construye tu trailer.",
        "directions": "Cómo llegar",
        "work_h": "Nuestro trabajo <em>reciente</em>",
        "work_p": "Eche un vistazo a nuestros últimos proyectos y vea cómo damos vida a las visiones culinarias con nuestros camiones de comida personalizables.",
        "prev": "Anterior", "next": "Siguiente", "delivered": "Trailer entregado",
        "work_alts": ["Clientes con su food trailer negro de La Patrona", "Clientes recibiendo su food trailer negro", "Collage de food trailers de La Patrona", "Mano con llavero de La Patrona frente a un trailer nuevo"],
        "rev_h": "Lo que dicen nuestros <em>clientes</em>",
        "rev_p": "Recomendaciones que nuestros clientes dejaron en Facebook, tal como las escribieron.",
        "rev_meta": "Recomienda La Patrona Trailers · Facebook · {date}",
        "finance": "Financiamiento de hasta $30K",
        "rev_btn": "Ver más en Facebook",
        "rev_alts": ["Reseña de un cliente en Facebook", "Reseña de un cliente en Facebook"],
        "founder_role": "CEO, La Patrona Trailers",
        "founder_h": "Sobre mí: Nathaly, <em>CEO de La Patrona Trailers</em>",
        "founder_alt": "Nathaly Lastra, fundadora y CEO de La Patrona Trailers",
        "founder_ps": [
            "Soy Nathaly, fundadora y CEO de La Patrona Trailers, y mi pasión es ayudar a los emprendedores a convertir sus sueños en realidad. He pasado años en la industria de los alimentos, adquiriendo un profundo conocimiento del mercado estadounidense, y he canalizado ese conocimiento para crear una empresa que represente la calidad, la innovación y la confianza.",
            "Para mí, comprender las necesidades únicas de cada cliente es la clave para crear soluciones personalizadas que realmente funcionen. Desde el momento en que comenzamos a diseñar un remolque hasta el momento en que sale a la carretera, mi equipo y yo estamos comprometidos a entregar más que un simple remolque. Brindamos una herramienta estratégica para el éxito de su negocio.",
            "En La Patrona Trailers no solo construimos camiones de comida, empoderamos a los emprendedores. Creo que cada negocio tiene una historia que contar y mi objetivo es brindarle las herramientas para escribir su propia historia de éxito. Mi visión es ayudar a las personas a dar ese primer paso hacia la independencia y la libertad financiera equipándolas con las mejores cocinas móviles.",
        ],
        "quote_text": "Invertir en un food truck no se trata solo de comprar un vehículo; se trata de construir un puente hacia tu libertad financiera y tus sueños empresariales. En La Patrona Trailers, no solo vendemos trailers, creamos oportunidades.",
        "quote_foot": "Una reflexión personal, Nathaly Lastra",
        "cta_h": "Construyamos tu <em>food trailer.</em>",
        "cta_btn": "Cotizar por WhatsApp",
        "contact_h": "Contactar a <em>La Patrona Trailers</em>",
        "contact_p": "Déjanos tus datos y en Lastra Multiservice LLC nos pondremos en contacto contigo.",
        "f": {"first": "Nombre", "last": "Apellidos", "phone": "Teléfono", "email": "Email", "city": "Ciudad"},
        "sms": "Acepto recibir mensajes SMS de La Patrona Trailers relacionados con mi cita, incluyendo confirmaciones, recordatorios y seguimientos. Los mensajes serán enviados hasta un máximo de 4 por cita, y pueden aplicarse tarifas de mensajes y datos. Responde STOP para cancelar en cualquier momento. Los mensajes se enviarán con la frecuencia necesaria para mantenerme informado sobre mi cita, lo que puede incluir recordatorios y actualizaciones importantes antes y después de la cita.",
        "accept": "He leído y acepto los", "terms": "Términos y Condiciones", "privacy_l": "Política de Privacidad",
        "send": "Enviar solicitud de contacto",
        "form_note": "En esta vista previa, al enviar se abre WhatsApp con tus datos.",
        "err_req": "Obligatorio.", "err_email": "Escribe un email válido.", "err_sum": "Completa los campos marcados.",
        "ok": "Abriendo WhatsApp con tus datos…",
        "wa_form": "¡Hola! Quisiera que La Patrona Trailers me contacte.",
        "policies_h": "Políticas", "schedule_h": "Horario", "contact_h2": "Contacto",
        "legal": [
            ("Política de privacidad", "politica-de-privacidad/"), ("Términos y condiciones de uso", "terminos-y-condiciones/"),
            ("Política de SMS", "politica-de-sms-mensajeria/"), ("Política de Cookies", "politica-de-cookies/"),
            ("Aviso Legal", "aviso-legal/"), ("Términos de Servicio", "terminos-de-servicio/"),
        ],
        "legal_base": "https://www.lapatronatrailers.com/es/",
        "hours": [("Lunes – Viernes", "11:00 AM – 3:00 PM · 4:30 PM – 10:00 PM"), ("Sábado – Domingo", "4:30 PM – 10:00 PM")],
        "to_top": "Volver arriba",
        "logo_alt": "Inicio de La Patrona Trailers",
    },
}


def crew(lo, hi):
    out = []
    for i in range(1, 6):
        cls = "" if i <= lo else ("maybe" if i <= hi else "off")
        out.append(icon("person", f"icon {cls}".strip(), filled=True))
    return f'<span class="crew">{"".join(out)}</span>'


def page(t):
    b = t["base"]
    L = t["lang"]
    accept_privacy = "He leído y acepto la" if L == "es" else t["accept"]
    label = lambda k: k.replace("x", " × ")

    hero_order = [SIZES[i] for i in (2, 3, 4, 0, 1)]  # open on the 8x14 studio shot
    hero_imgs = "\n".join(
        f'        <img src="{b}assets/img/trailer-{k}-sm.webp" alt="" data-len="{n}" data-label="{label(k)} {t["ft"].upper()}" width="900" height="620"{" fetchpriority=\"high\"" if i == 0 else " loading=\"lazy\""}>'
        for i, (k, n, _, _) in enumerate(hero_order)
    )

    tabs = "\n".join(
        f'        <button type="button" role="tab" id="tab-{k}" aria-controls="size-{k}" aria-selected="{"true" if i == 0 else "false"}">{label(k)}</button>'
        for i, (k, *_) in enumerate(SIZES)
    )

    panels = []
    for k, n, lo, hi in SIZES:
        tag, desc, cap = t["sizes"][k]
        scale = 58 + 42 * (n - 10) / 10
        s = label(k)
        panels.append(f'''      <article class="size-panel" id="size-{k}" role="tabpanel" aria-labelledby="tab-{k}" tabindex="0">
        <div class="size-visual">
          <div class="photo"><img src="{b}assets/img/trailer-{k}.webp" alt="{s} {t['ft']} food trailer" style="--scale:{scale:.0f}%" loading="lazy" width="950" height="700"></div>
          <div class="ruler" style="--len:{n / 20 * 100:.0f}%" aria-hidden="true">
            <span class="tag mono">{n} {t['ft']} {t['length']}</span>
            <div class="scale"><span class="fill"></span></div>
            <div class="marks mono"><span>0</span><span>5</span><span>10</span><span>15</span><span>20 {t['ft']}</span></div>
          </div>
        </div>
        <div class="size-copy">
          <h3 class="size-name">{s}<small>{t['ft']}</small></h3>
          <p class="size-tagline">{tag}</p>
          <p class="size-desc">{desc}</p>
          <dl class="spec">
            <dt>{t['dims']}</dt><dd class="mono">8 {t['ft']} × {n} {t['ft']}</dd>
            <dt>{t['crew']}</dt><dd>{crew(lo, hi)}<span>{cap}</span></dd>
          </dl>
          <div class="btn-pair">
            <a class="btn btn-gold btn-lg" href="{wa(t['wa_size'].format(s=s.replace(' ', '')))}" target="_blank" rel="noopener">{t['quote_size'].format(s=s.replace(' ', ''))}</a>
            <a class="btn btn-gold btn-lg btn-square" href="{wa(t['wa_size'].format(s=s.replace(' ', '')))}" target="_blank" rel="noopener" aria-hidden="true" tabindex="-1">{icon('arrow')}</a>
          </div>
        </div>
      </article>''')
    panels = "\n".join(panels)

    apart = "\n".join(f'            <li><strong>{h}</strong><p>{p}</p></li>' for h, p in t["apart"])
    work_html = "\n".join(
        f'        <figure><img src="{b}assets/img/{w}.webp" alt="{t["work_alts"][i]}" loading="lazy" width="{wd}" height="{ht}"><figcaption>{t["delivered"]}</figcaption></figure>'
        for i, (w, wd, ht) in enumerate([("work-1", 653, 463), ("work-2", 550, 393)])
    )
    reviews_html = "\n".join(
        f'''          <figure class="review" lang="{lg}">
            <blockquote><p>{txt}</p></blockquote>
            <figcaption><strong>{name}</strong><span>{t["rev_meta"].format(date=date[L])}</span></figcaption>
          </figure>'''
        for name, date, lg, txt in REVIEWS
    )
    founder_ps = "\n".join(f'          <p class="lede">{p}</p>' for p in t["founder_ps"])
    legal = "\n".join(f'            <li><a href="{t["legal_base"]}{u}">{n}</a></li>' for n, u in t["legal"])
    hours = "\n".join(f'            <li class="hours">{d}<span>{h}</span></li>' for d, h in t["hours"])
    nav_ids = ["trailers", "custom", "about", "work", "founder"]
    nav = "\n".join(f'      <a class="btn" href="#{i}">{n}</a>' for i, n in zip(nav_ids, t["nav"]))
    f = t["f"]

    return f'''<!doctype html>
<html lang="{L}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>{t['title']}</title>
  <meta name="description" content="{t['desc']}">
  <meta name="theme-color" content="#060606">
  <link rel="alternate" hreflang="en" href="{b}">
  <link rel="alternate" hreflang="es" href="{b}es/">
  <link rel="icon" type="image/png" href="{b}assets/img/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
  <link rel="stylesheet" href="{b}assets/css/site.css">
  <script defer src="{b}assets/js/site.js"></script>
</head>
<body>
  <a class="skip" href="#main">{t['skip']}</a>

  <header class="site-header">
    <div class="brand-row">
      <a class="brand" href="{b if b else './'}{'es/' if L == 'es' else ''}" aria-label="{t['logo_alt']}">
        <img src="{b}assets/img/logo.webp" alt="" width="52" height="52">
        <span>La Patrona<br>Trailers</span>
      </a>
      <nav class="lang" aria-label="Language">
        <a href="{'./' if L == 'en' else '../'}" hreflang="en" lang="en" aria-current="{'true' if L == 'en' else 'false'}">English</a>
        <a href="{'es/' if L == 'en' else './'}" hreflang="es" lang="es" aria-current="{'true' if L == 'es' else 'false'}">Español</a>
      </nav>
    </div>
    <nav class="nav" aria-label="Main">
{nav}
    </nav>
    <div class="header-cta">
      <a class="btn" href="#contact">{t['contact']}</a>
      <a class="btn btn-call" href="tel:+{PHONE}" aria-label="{t['call']}">{icon('phone')}</a>
      <a class="btn btn-gold btn-quote" href="{t['quote_url']}" target="_blank" rel="noopener">{t['quote']}</a>
    </div>
  </header>

  <main id="main">
    <section class="hero">
      <div class="hero-stage">
        <div class="capsule">
          <h1><span class="hero-word">{t['hero_words'][0]}</span><span class="hero-word">{t['hero_words'][1]}</span></h1>
          <div class="hero-trailers">
{hero_imgs}
          </div>
          <div class="hero-readout" aria-hidden="true">
            <span class="size mono">8 × 14 {t['ft'].upper()}</span>
            <div class="ruler-mini"><span></span></div>
          </div>
        </div>
      </div>
      <div class="hero-foot">
        <div class="hero-intro">
          <p>{t['hero_l1']}</p>
          <p>{t['hero_l2']}</p>
          <div class="btn-pair">
            <a class="btn btn-gold btn-lg" href="{t['quote_url']}" target="_blank" rel="noopener">{t['quote']}</a>
            <a class="btn btn-gold btn-lg btn-square" href="{t['quote_url']}" target="_blank" rel="noopener" aria-hidden="true" tabindex="-1">{icon('arrow')}</a>
          </div>
        </div>
        <a class="scroll-cue" href="#trailers"><span class="dot"></span>{t['scroll']}</a>
      </div>
    </section>

    <section class="section sizes" id="trailers" aria-labelledby="offer-h">
      <div class="split-head">
        <h2 class="display" id="offer-h">{t['offer_h']}</h2>
        <p class="lede">{t['offer_p']}</p>
      </div>
      <div class="size-tabs" role="tablist" aria-label="{t['tabs_label']}">
{tabs}
        <button type="button" class="custom" data-jump="#custom">{t['custom_tab']} →</button>
      </div>
      <div class="size-panels">
{panels}
      </div>
    </section>

    <section class="section-tight custom-band" id="custom" aria-labelledby="custom-h" style="padding-inline: var(--gutter)">
      <div class="custom-frame">
        <div class="custom-copy">
          <h2 class="display" id="custom-h">{t['custom_h']}</h2>
          <p class="lede">{t['custom_p']}</p>
          <div class="btn-pair">
            <a class="btn btn-gold btn-lg" href="{wa(t['wa_custom'])}" target="_blank" rel="noopener">{t['custom_btn']}</a>
            <a class="btn btn-gold btn-lg btn-square" href="{wa(t['wa_custom'])}" target="_blank" rel="noopener" aria-hidden="true" tabindex="-1">{icon('arrow')}</a>
          </div>
        </div>
        <figure class="custom-art"><img src="{b}assets/img/personalized.webp" alt="{t['custom_alt']}" loading="lazy" width="1024" height="875"></figure>
      </div>
    </section>

    <section class="section" id="about" aria-label="{t['nav'][2]}">
      <h2 class="statement">{t['about_h']}</h2>
      <div class="about-grid">
        <div>
          <p class="lede">{t['about_p1']}</p>
          <p class="lede">{t['about_p2']}</p>
        </div>
        <div class="apart">
          <h3 class="h3">{t['apart_h']}</h3>
          <ul>
{apart}
          </ul>
        </div>
      </div>
      <div class="visit">
        {icon('pin')}
        <p>{t['visit_t']}<span>2900 Titan Row, Suite 130, Orlando, FL 32817</span></p>
        <a class="btn btn-lg" href="{MAPS}" target="_blank" rel="noopener">{t['directions']} {icon('arrow')}</a>
      </div>
    </section>

    <section class="section-tight" id="work" aria-labelledby="work-h" style="padding-inline: var(--gutter)">
      <div class="work-head">
        <h2 class="display" id="work-h">{t['work_h']}</h2>
        <p class="lede">{t['work_p']}</p>
      </div>
      <div class="work-grid">
{work_html}
      </div>
    </section>

    <section class="section" aria-labelledby="rev-h">
      <div class="reviews">
        <div>
          <h2 class="display" id="rev-h">{t['rev_h']}</h2>
          <p class="lede">{t['rev_p']}</p>
          <div class="btn-pair">
            <a class="btn btn-lg" href="{FACEBOOK}" target="_blank" rel="noopener">{icon('fb')} {t['rev_btn']}</a>
          </div>
        </div>
        <div class="review-list">
{reviews_html}
        </div>
      </div>
    </section>

    <section class="section" id="founder" aria-labelledby="founder-h" style="padding-top:0">
      <div class="founder">
        <figure class="founder-photo">
          <div class="stage"><img src="{b}assets/img/nathaly-cutout.webp" alt="{t['founder_alt']}" loading="lazy" width="495" height="1271"></div>
          <figcaption><strong>Nathaly Lastra</strong><span>{t['founder_role']}</span></figcaption>
        </figure>
        <div class="founder-copy">
          <h2 class="display" id="founder-h" style="font-size:clamp(36px,4.2vw,72px)">{t['founder_h']}</h2>
{founder_ps}
          <blockquote class="quote">
            <p>{t['quote_text']}</p>
            <footer>{t['quote_foot']}</footer>
          </blockquote>
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="cta-h">
      <h2 class="display" id="cta-h">{t['cta_h']}</h2>
      <p class="finance mono">{t['finance']}</p>
      <div class="btn-pair">
        <a class="btn btn-gold btn-lg" href="{t['quote_url']}" target="_blank" rel="noopener">{icon('chat')} {t['cta_btn']}</a>
        <a class="btn btn-gold btn-lg btn-square" href="{t['quote_url']}" target="_blank" rel="noopener" aria-hidden="true" tabindex="-1">{icon('arrow')}</a>
      </div>
    </section>

    <section class="section" id="contact" aria-labelledby="contact-h">
      <div class="contact">
        <div class="contact-info">
          <h2 class="display" id="contact-h">{t['contact_h']}</h2>
          <p class="lede">{t['contact_p']}</p>
          <ul class="contact-list">
            <li>{icon('phone')}<a href="tel:+{PHONE}">+1 (863) 266-9575</a></li>
            <li>{icon('mail')}<a href="mailto:lapatronatrailers@gmail.com">lapatronatrailers@gmail.com</a></li>
            <li>{icon('pin')}<a href="{MAPS}" target="_blank" rel="noopener">2900 Titan Row, Suite 130<span>Orlando, FL 32817</span></a></li>
            <li>{icon('clock')}<div>{t['hours'][0][0]}<span>{t['hours'][0][1]}</span>{t['hours'][1][0]}<span>{t['hours'][1][1]}</span></div></li>
          </ul>
        </div>
        <form class="form" novalidate
          data-err-required="{t['err_req']}" data-err-email="{t['err_email']}" data-err-summary="{t['err_sum']}" data-ok="{t['ok']}"
          data-wa-intro="{t['wa_form']}" data-l-name="{f['first']}" data-l-phone="{f['phone']}" data-l-email="{f['email']}" data-l-city="{f['city']}">
          <div class="field"><label for="f-first">{f['first']}</label><input id="f-first" name="first" autocomplete="given-name" required><span class="err" id="f-first-err" aria-live="polite"></span></div>
          <div class="field"><label for="f-last">{f['last']}</label><input id="f-last" name="last" autocomplete="family-name" required><span class="err" id="f-last-err" aria-live="polite"></span></div>
          <div class="field"><label for="f-phone">{f['phone']}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><span class="err" id="f-phone-err" aria-live="polite"></span></div>
          <div class="field"><label for="f-email">{f['email']}</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err" id="f-email-err" aria-live="polite"></span></div>
          <div class="field full"><label for="f-city">{f['city']}</label><input id="f-city" name="city" autocomplete="address-level2" required><span class="err" id="f-city-err" aria-live="polite"></span></div>
          <div class="checks">
            <label class="check"><input type="checkbox" name="sms" id="f-sms"><span>{t['sms']}</span></label>
            <label class="check"><input type="checkbox" name="terms" id="f-terms" required><span>{t['accept']} <a href="{t['legal_base']}{t['legal'][1][1]}" target="_blank" rel="noopener">{t['terms']}</a></span></label>
            <label class="check"><input type="checkbox" name="privacy" id="f-privacy" required><span>{accept_privacy} <a href="{t['legal_base']}{t['legal'][0][1]}" target="_blank" rel="noopener">{t['privacy_l']}</a></span></label>
          </div>
          <p class="form-status" role="status"></p>
          <div class="form-foot">
            <p>{t['form_note']}</p>
            <button class="btn btn-gold btn-lg" type="submit">{t['send']}</button>
          </div>
        </form>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-grid">
      <div><img src="{b}assets/img/logo.webp" alt="La Patrona Trailers" width="120" height="120" loading="lazy"></div>
      <div>
        <h2>{t['policies_h']}</h2>
        <ul>
{legal}
        </ul>
      </div>
      <div>
        <h2>{t['schedule_h']}</h2>
        <ul>
{hours}
        </ul>
      </div>
      <div>
        <h2>{t['contact_h2']}</h2>
        <ul>
          <li>2900 Titan Row, Suite 130, Orlando FL 32817</li>
          <li><a href="tel:+{PHONE}">+1 (863) 266-9575</a></li>
          <li><a href="mailto:lapatronatrailers@gmail.com">lapatronatrailers@gmail.com</a></li>
          <li><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 La Patrona Trailers · Lastra Multiservice LLC</span>
      <a class="to-top" href="#main">{t['to_top']} {icon('up')}</a>
    </div>
  </footer>

  <div class="quote-bar">
    <a class="btn btn-gold" href="{t['quote_url']}" target="_blank" rel="noopener">{icon('chat')} {t['quote']}</a>
    <a class="btn" href="tel:+{PHONE}" aria-label="{t['call']}">{icon('phone')}</a>
  </div>
</body>
</html>
'''


if __name__ == "__main__":
    (ROOT / "index.html").write_text(page(T["en"]), encoding="utf-8")
    (ROOT / "es").mkdir(exist_ok=True)
    (ROOT / "es" / "index.html").write_text(page(T["es"]), encoding="utf-8")
    print("built index.html, es/index.html")
