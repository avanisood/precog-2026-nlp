import os
import re

# --- CONFIGURATION ---
INPUT_DIR = "raw_data_1890s"
OUTPUT_DIR = "clean_data_smart_merge"
MIN_WORDS = 100  # Strict lower bound from Task 0.3
MAX_WORDS = 250  # Slightly higher to allow natural sentence endings

def smart_clean_and_merge(raw_text):
    # 1. EXTRACT MAIN TEXT (Remove Gutenberg License)
    start_match = re.search(r'\*\*\* START OF (THE|THIS) PROJECT GUTENBERG EBOOK .* \*\*\*', raw_text)
    end_match = re.search(r'\*\*\* END OF (THE|THIS) PROJECT GUTENBERG EBOOK .* \*\*\*', raw_text)
    
    if start_match and end_match:
        main_text = raw_text[start_match.end():end_match.start()]
    else:
        main_text = raw_text

    # 2. IDENTIFY NATURAL PARAGRAPHS
    # Split by double newlines (standard Gutenberg formatting)
    raw_paragraphs = main_text.split('\n\n')
    
    # Clean individual paragraphs (unwrap lines, remove debris)
    clean_paragraphs = []
    for p in raw_paragraphs:
        # Flatten lines: "The quick\nbrown fox" -> "The quick brown fox"
        clean_p = p.replace('\n', ' ').strip()
        clean_p = re.sub(r'\s+', ' ', clean_p) # Remove multi-spaces
        
        # Filter out Chapter titles or Metadata debris
        if len(clean_p) > 20 and "Chapter" not in clean_p and "Project Gutenberg" not in clean_p:
            clean_paragraphs.append(clean_p)

    # 3. SMART MERGE LOOP
    # Combine short paragraphs (dialogue) until we hit MIN_WORDS
    final_samples = []
    current_buffer = ""
    current_word_count = 0
    
    for p in clean_paragraphs:
        # Add this paragraph to our buffer
        # We add a newline marker to show where the original break was (optional preservation)
        if current_buffer:
            current_buffer += " " + p
        else:
            current_buffer = p
            
        current_word_count = len(current_buffer.split())
        
        # CHECK: Is it big enough yet?
        if current_word_count >= MIN_WORDS:
            # It is big enough. Is it TOO big?
            if current_word_count <= MAX_WORDS:
                # Perfect size. Save it.
                final_samples.append(current_buffer)
                current_buffer = ""
                current_word_count = 0
            else:
                # It's too big (e.g. 400 words). We must save it, but acknowledge it's large.
                # Or, strictly discard it if you want perfect data. 
                # Here, we save it because preserving author flow is your goal.
                final_samples.append(current_buffer)
                current_buffer = ""
                current_word_count = 0
    
    return final_samples

# --- EXECUTION ---
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]
    
    for filename in files:
        filepath = os.path.join(INPUT_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()
            
        samples = smart_clean_and_merge(raw)
        
        # Stats Check
        if samples:
            avg_len = sum(len(s.split()) for s in samples) / len(samples)
            print(f"✅ {filename}: {len(samples)} samples generated.")
            print(f"   Avg Words: {avg_len:.1f} (Target: 100-200)")
        
        # Save
        save_path = os.path.join(OUTPUT_DIR, f"SMART_{filename}")
        with open(save_path, 'w', encoding='utf-8') as out:
            out.write("\n|||\n".join(samples))