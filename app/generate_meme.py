def match_template(prompt_or_caption):
    prompt_or_caption = prompt_or_caption.lower()

    if "drake" in prompt_or_caption or "prefer" in prompt_or_caption:
        return "181913649"  # Drakeposting
    elif "distracted" in prompt_or_caption or "boyfriend" in prompt_or_caption:
        return "112126428"  # Distracted Boyfriend
    elif "two buttons" in prompt_or_caption or "confused" in prompt_or_caption:
        return "87743020"   # Two Buttons
    elif "no one" in prompt_or_caption or "literally no one" in prompt_or_caption:
        return "131087935"  # Running Away Balloon
    elif "change my mind" in prompt_or_caption:
        return "129242436"
    else:
        return "181913649"  # Default to Drakeposting
