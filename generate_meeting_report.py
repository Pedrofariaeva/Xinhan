#!/usr/bin/env python3
"""Generate Meeting Report bilingual document from V03 English."""

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


def set_run_format(run, bold=False, size_pt=None, italic=False):
    run.bold = bold
    run.italic = italic
    if size_pt:
        run.font.size = Pt(size_pt)


def add_para(doc, text, align=None, bold=False, size_pt=None, space_before=None, space_after=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if space_before is not None:
        p.paragraph_format.space_before = Pt(space_before)
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    set_run_format(run, bold=bold, size_pt=size_pt)
    return p


def add_table_row(table, cells):
    row = table.add_row()
    for i, text in enumerate(cells):
        if i < len(row.cells):
            row.cells[i].text = text


def generate_meeting_report():
    doc = Document()

    # Title
    add_para(doc, '会议纪要', align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size_pt=18)
    add_para(doc, 'MEETING REPORT', align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size_pt=18)
    doc.add_paragraph()

    # Header info
    add_para(doc, '日期：2026年6月2日')
    add_para(doc, 'Date: 2nd June 2026')
    add_para(doc, '主题：Pedro Faria（方础予）合同履约情况分析')
    add_para(doc, 'Subject: Analysis on Contract Status of Pedro Faria (方础予)')
    add_para(doc, '出席人员：刘蒙蒙（Mengmeng Liu）、孟秀凡（Xiufan Meng）、方础予（Pedro Faria）')
    add_para(doc, 'Attendance: Mengmeng Liu, Xiufan Meng, Pedro Faria')
    add_para(doc, '会议地点：海甸校区田家炳楼')
    add_para(doc, 'Location: Tianjiabing Building, Haidian Campus')
    doc.add_paragraph()

    # Section 1
    add_para(doc, '1. 会议目的', bold=True, size_pt=12, space_before=12, space_after=6)
    add_para(doc, '1. Purpose of the Meeting', bold=True, size_pt=12, space_after=6)

    add_para(doc, '本次会议旨在审查员工方础予（Pedro Faria）的工作表现及合同履约情况。', space_before=10, space_after=10)
    add_para(doc, 'The purpose of the meeting was to review the performance and contractual compliance of the employee Pedro Faria (方础予).', space_before=10, space_after=10)

    add_para(doc, '会议涵盖以下内容：', space_before=10, space_after=10)
    add_para(doc, 'The following contents were covered:', space_before=10, space_after=10)

    add_para(doc, '审查Pedro的合同条款，评估各项任务已完成、进行中或未完成的状况。', space_before=10, space_after=10)
    add_para(doc, "Reviewed Pedro's contract terms and assessed if a task was completed, ongoing or not done.", space_before=10, space_after=10)

    add_para(doc, '分析当前情况，调整工作任务以适应最新形势，并努力匹配原工作合同义务，以规避未来审计风险。', space_before=10, space_after=10)
    add_para(doc, 'Analyzed current situation, adjusted the working task fitting latest situation and tried to match the original working contract obligation and to avoid future audit risk.', space_before=10, space_after=10)

    # Section 2
    add_para(doc, '2. 确定的工作成果', bold=True, size_pt=12, space_before=12, space_after=6)
    add_para(doc, '2. Defined Outputs', bold=True, size_pt=12, space_after=6)

    add_para(doc, '会议期间具体讨论并重新调整了以下义务与职责：', space_before=10, space_after=10)
    add_para(doc, 'Specifically, the following obligations and duties were discussed and realigned during meeting:', space_before=10, space_after=10)

    # CN Table
    cn_table = doc.add_table(rows=1, cols=4)
    cn_table.style = 'Table Grid'
    cn_table.rows[0].cells[0].text = '序号'
    cn_table.rows[0].cells[1].text = '状态'
    cn_table.rows[0].cells[2].text = '交付成果'
    cn_table.rows[0].cells[3].text = '目标日期'
    add_table_row(cn_table, ['1', '（待确认）', '考虑翻译梅西大学此前提供的设计任务书样本——须确认原始文件。', '（待定）'])
    add_table_row(cn_table, ['2', '初稿已完成', '技术规范书中英文版本修订', '2026年6月21日'])
    add_table_row(cn_table, ['3', '进行中', '崖州校区前期设计任务书评析报告——须完成中英文终版文件（报告日期：2025年5月21日）', '2026年6月21日'])
    add_table_row(cn_table, ['4', '待开展', '汇总欧盟、英国、澳大拉西亚及美国动物住房动物福利要求文件或官方网站', '2026年7月3日'])

    doc.add_paragraph()

    # EN Table
    en_table = doc.add_table(rows=1, cols=4)
    en_table.style = 'Table Grid'
    en_table.rows[0].cells[0].text = 'No.'
    en_table.rows[0].cells[1].text = 'Status'
    en_table.rows[0].cells[2].text = 'Deliverable'
    en_table.rows[0].cells[3].text = 'Target Date'
    add_table_row(en_table, ['1', '', 'Consider translating the design brief samples provided by Massey University previously) – need to identify the original documents.', ''])
    add_table_row(en_table, ['2', 'First Draft Done', 'Revision on the booklet in both Chinese and English versions', '21st June 2026'])
    add_table_row(en_table, ['3', 'Ongoing', 'Commentary report/Analysis on previous Yazhou Campus design brief- in both Chinese and English version — Report dated 21st May 2025 - to be finished final document', '21st June 2026'])
    add_table_row(en_table, ['4', 'To be developed', 'Summarize animal welfare requirement documents or official websites for animal housing in the EU, UK, AUTRALASIAN, USA', '3rd July 2026'])

    doc.add_paragraph()

    # Section 3
    add_para(doc, '3. 拟新增研究领域', bold=True, size_pt=12, space_before=12, space_after=6)
    add_para(doc, '3. Proposed New Research Areas', bold=True, size_pt=12, space_after=6)

    add_para(doc, '已规划以下研究课题：', space_before=10, space_after=10)
    add_para(doc, 'The following research topics were planned:', space_before=10, space_after=10)

    add_para(doc, '3.1 住宅物体检测技术——Astrolaby（阿斯卓拉比）', space_before=10, space_after=6)
    add_para(doc, '3.1 Housing Object Detection Technology — Astrolaby', space_before=10, space_after=6)

    add_para(doc, '说明：将用于住宅物体检测的技术（Astrolaby——个人开发项目）进行改造，以支持养老住宅及建筑功能需求。', space_before=10, space_after=10)
    add_para(doc, 'Description: Adaptation of technology developed for housing object detection (Astrolaby — personal development project) to support senior housing and architectural functionality.', space_before=10, space_after=10)

    add_para(doc, '状态：提请曾主任审批或进一步指导', space_before=10, space_after=10)
    add_para(doc, 'Status: Proposed for approval or further advice from Director Zeng', space_before=10, space_after=10)

    add_para(doc, '3.2 海上及海下建筑材料性能汇编', space_before=10, space_after=6)
    add_para(doc, '3.2 Compendium on Materials Performance for Construction Under and Over the Sea', space_before=10, space_after=6)

    add_para(doc, '内容摘要：着眼于未来在海上及海下进行可持续建设的远景目标，须明确界定某些基础性条件与指标。这些指标包括：材料使用寿命、可再利用性、对人类及动物生命的影响能力、类型学与可改造性、能源效率、环境影响及其他相关因素。本汇编将生成大规模信息数据集，为未来建设及决策提供支持。计划以在线形式发布，并开放获取。', space_before=10, space_after=10)
    add_para(doc, 'Short Abstract: > With the future aim of constructing sustainable developments both under and over the sea, certain foundational conditions and indicators must be defined. These include lifespan, reusability, capacity to impact human and animal life, typologies and transformation capacity, energy efficiency, environmental impact, and other relevant factors. > > This Compendium will generate a large dataset of information to support future construction and decision-making. It is intended to be published online with open access.', space_before=10, space_after=10)

    add_para(doc, '状态：提请曾主任审批或进一步指导', space_before=10, space_after=10)
    add_para(doc, 'Status: Proposed for approval or further advice from Director Zeng', space_before=10, space_after=10)

    # Section 4
    add_para(doc, '4. 下一步工作', bold=True, size_pt=12, space_before=12, space_after=6)
    add_para(doc, '4. Next Steps', bold=True, size_pt=12, space_after=6)

    add_para(doc, '在接下来两周内完成技术规范书及崖州校区前期设计任务书评析报告（中英文版本），并将终版发送至建设部同事进一步讨论。', space_before=10, space_after=10)
    add_para(doc, 'Work on the booklet and "Commentary report/Analysis on previous Yazhou Campus design brief- in both Chinese and English version in next 2 weeks, send the final version to colleagues in Construction Department for further discussion.', space_before=10, space_after=10)

    add_para(doc, '于七月中旬提交欧盟、英国、澳大拉西亚及美国动物住房动物福利要求文件或官方网站的汇总报告。', space_before=10, space_after=10)
    add_para(doc, 'Send the summary report of Summarize animal welfare requirement documents or official websites for animal housing in the EU, UK, AUTRALASIAN, USA in mid-July', space_before=10, space_after=10)

    add_para(doc, '为拟开展的研究课题（Astrolaby养老住宅适配项目及海上建筑材料汇编）准备充分的背景资料，但首先须就后续推进方式获得进一步指导。', space_before=10, space_after=10)
    add_para(doc, 'Prepare substantiate background for the proposed research topics (Astrolaby senior housing adaptation and Marine Construction Materials Compendium), although some further advice on how to proceed will be required first.', space_before=10, space_after=10)

    add_para(doc, '就第四章延期事项安排后续跟进会议。', space_before=10, space_after=10)
    add_para(doc, 'Schedule follow-up meeting for postponed Chapter 4 items.', space_before=10, space_after=10)

    output_path = 'uncoveredDocs/MeetingReport_20260602_Bilingual_V20260609.docx'
    doc.save(output_path)
    print(f'Saved: {output_path}')


if __name__ == '__main__':
    generate_meeting_report()
