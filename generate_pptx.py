import re
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def set_dark_theme(slide):
    # Set dark navy background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(10, 25, 47)  # Dark navy

def format_text_frame(text_frame, text, is_title=False):
    text_frame.word_wrap = True
    p = text_frame.paragraphs[0]
    p.text = text
    p.font.name = 'Arial'
    p.font.color.rgb = RGBColor(255, 255, 255)
    
    if is_title:
        p.font.size = Pt(40)
        p.font.bold = True
    else:
        p.font.size = Pt(20)

def add_bullet_points(text_frame, lines):
    for i, line in enumerate(lines):
        if not line.strip(): continue
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()
        p.text = line.replace('* ', '').strip()
        p.font.name = 'Arial'
        p.font.size = Pt(20)
        p.font.color.rgb = RGBColor(255, 255, 255)
        if line.strip().startswith('*') or line.strip().startswith('-') or bool(re.match(r'^\d+\.', line.strip())):
            p.level = 0
            
def main():
    prs = Presentation()
    
    # Read the markdown file
    md_path = r'c:\Users\johnl\OneDrive\Desktop\EMERGING REPORT\serverless_presentation.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split by slides
    slides_data = re.split(r'## SLIDE \d+ —[^\n]+', content)
    slides_data = [s.strip() for s in slides_data if s.strip()]
    
    if len(slides_data) > 20: # First block might be intro text
        slides_data = slides_data[1:]
        
    for slide_data in slides_data:
        # Extract title
        title_match = re.search(r'\*\*Title:\*\*\s*(.*)', slide_data)
        title = title_match.group(1).strip() if title_match else "Serverless Computing"
        
        # Extract subtitle if any
        subtitle_match = re.search(r'\*\*Subtitle:\*\*\s*(.*)', slide_data)
        subtitle = subtitle_match.group(1).strip() if subtitle_match else ""
        
        # Extract content
        content_match = re.search(r'\*\*Content:\*\*\s*(.*?)(?=\*\*Visual Description:|\*\*Question|\*\*Speaker Notes:|\Z)', slide_data, re.DOTALL)
        slide_content = content_match.group(1).strip() if content_match else ""
        
        # In Slide 1, content might not have **Content:**, check for **Presented by:**
        if "Presented by:" in slide_data:
            content_match = re.search(r'\*\*Presented by:\*\*(.*?)(?=\*\*Visual Description:|\*\*Speaker Notes:)', slide_data, re.DOTALL)
            slide_content = "Presented by:\n" + content_match.group(1).strip() if content_match else ""
            
        # Add questions to slide content if present
        question_match = re.search(r'\*\*Question \d+:\*\*(.*?)(?=\*\*Speaker Notes:|\Z)', slide_data, re.DOTALL)
        if question_match:
            question_text = question_match.group(1).strip()
            slide_content += "\n\nKnowledge Check:\n" + question_text.replace('*', '')

        # For the "Final Knowledge Check" slide
        if "What is serverless computing?" in slide_data and "Final Knowledge Check" in slide_data:
            slide_content = "1. What is serverless computing?\n2. What does FaaS stand for?\n3. What does BaaS stand for?\n4. Why is automatic scaling an advantage?\n5. Is serverless computing the same thing as cloud computing?"
            
        # Extract speaker notes
        notes_match = re.search(r'\*\*Speaker Notes:\*\*\s*(.*)', slide_data, re.DOTALL)
        notes = notes_match.group(1).strip() if notes_match else ""
        notes = notes.replace('>', '').strip()
        
        # Create slide
        # Using layout 1 for Title slide (Slide 1 and 20), layout 5 (Title only) or layout 6 (Blank) to customize
        if "TITLE SLIDE" in slide_data or slide_content.startswith("Presented by:") or "Thank You" in title:
            slide_layout = prs.slide_layouts[0] # Title slide
            slide = prs.slides.add_slide(slide_layout)
            set_dark_theme(slide)
            
            title_shape = slide.shapes.title
            format_text_frame(title_shape.text_frame, title, is_title=True)
            
            if len(slide.placeholders) > 1:
                sub = slide.placeholders[1]
                sub_text = subtitle + "\n" + slide_content if subtitle else slide_content
                format_text_frame(sub.text_frame, sub_text.replace('**', ''))
        else:
            slide_layout = prs.slide_layouts[1] # Title and Content
            slide = prs.slides.add_slide(slide_layout)
            set_dark_theme(slide)
            
            title_shape = slide.shapes.title
            format_text_frame(title_shape.text_frame, title, is_title=True)
            
            body_shape = slide.placeholders[1]
            lines = [line.strip() for line in slide_content.split('\n') if line.strip()]
            
            add_bullet_points(body_shape.text_frame, lines)
            
        # Add notes
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes
        
    out_path = r'c:\Users\johnl\OneDrive\Desktop\EMERGING REPORT\SERVERLESS_COMPUTING_REPORT.pptx'
    prs.save(out_path)
    print(f"Presentation saved successfully to {out_path}")

if __name__ == '__main__':
    main()
