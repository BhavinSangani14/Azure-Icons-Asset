import os
import shutil

def collect_all_svg_icons_same_name(
    source_base="D:\Azure Icons\static\images\Icons", 
    destination="svg"
):
    os.makedirs(destination, exist_ok=True)

    for category in os.listdir(source_base):
        svg_dir = os.path.join(source_base, category, "svg")
        if not os.path.isdir(svg_dir):
            continue

        for file in os.listdir(svg_dir):
            if file.lower().endswith(".svg"):
                source_path = os.path.join(svg_dir, file)
                dest_path = os.path.join(destination, file)

                if not os.path.exists(dest_path):
                    shutil.copy2(source_path, dest_path)

    print(f"✅ All SVGs copied to: {destination} (duplicates skipped)")

# Run it
collect_all_svg_icons_same_name()
