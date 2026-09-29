from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / "Devyansh_Gupta_Terraform_Course_Project_Report.pdf"
SCREENSHOT = Path(r"C:\Users\Admin\AppData\Local\Temp\codex-clipboard-7b7172f6-b4ec-48f8-95c4-1fbfc7d8d1dc.png")
blue = colors.HexColor("#135da8")
navy = colors.HexColor("#1f2933")
light = colors.HexColor("#eef4fb")
grey = colors.HexColor("#5b6570")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBlue", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=21, leading=26, textColor=blue, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="HeadingBlue", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=blue, spaceBefore=8, spaceAfter=9))
styles.add(ParagraphStyle(name="HeadingDark", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=navy, spaceBefore=6, spaceAfter=5))
styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=14, textColor=navy, spaceAfter=7))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, textColor=navy, spaceAfter=8))
styles.add(ParagraphStyle(name="CenterSmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=13, alignment=TA_CENTER, textColor=grey))
def p(text, style="Body"):
    return Paragraph(text, styles[style])
def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d7dde5"))
    canvas.line(0.55*inch, 0.55*inch, 7.95*inch, 0.55*inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(grey)
    canvas.drawString(0.6*inch, 0.35*inch, "Programming for Cloud Platform | Activity - 1")
    canvas.drawRightString(7.9*inch, 0.35*inch, str(doc.page))
    canvas.restoreState()
def title_block(title, subtitle=None):
    items = [p(title, "HeadingBlue")]
    if subtitle:
        items.append(p(subtitle, "CenterSmall"))
    items.append(Spacer(1, 10))
    return items
def grid(data, widths):
    t = Table(data, colWidths=widths, hAlign="CENTER")
    t.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.6, colors.HexColor("#b8c4d2")), ("BACKGROUND", (0,0), (-1,0), blue), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"), ("FONTSIZE", (0,0), (-1,-1), 9), ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, light]), ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8)]))
    return t
story = []
story += [Spacer(1, 0.35*inch), p("School of Computer Science and Information Technology", "TitleBlue"), p("Department of Computer Science and Information Technology", "CenterSmall"), Spacer(1, 0.42*inch)]
cover = [[p("Semester:", "BodySmall"), p("III", "BodySmall")], [p("Specialisation:", "BodySmall"), p("SCT", "BodySmall")], [p("Subject:", "BodySmall"), p("Programming for Cloud Platform", "BodySmall")]]
story += [grid(cover, [1.5*inch, 4.5*inch]), Spacer(1, 0.35*inch), p("Activity - 1", "TitleBlue"), p("Course with Project", "CenterSmall"), Spacer(1, 0.35*inch)]
cover_info = [[p("Date of Submission:", "BodySmall"), p("27-09-2026", "BodySmall")], [p("Submitted by:", "BodySmall"), p("Name: Devyansh Gupta<br/>USN No: 25MCAR0193", "BodySmall")], [p("Faculty In-Charge", "BodySmall"), p("Dr. Pushpa J", "BodySmall")], [p("Course:", "BodySmall"), p("HashiCorp Certified: Terraform Associate (003) Cert Prep by KodeKloud", "BodySmall")]]
story += [grid(cover_info, [1.7*inch, 4.3*inch]), Spacer(1, 0.35*inch), p("Signature: ________________________________", "BodySmall"), PageBreak()]
story += title_block("CERTIFICATE")
story += [p("This is to certify that Mr. Devyansh Gupta has satisfactorily completed the activity prescribed by JAIN (Deemed to be University) for the Third semester degree course in the year 2026. The activity is based on HashiCorp Certified: Terraform Associate (003) Cert Prep by KodeKloud and its accompanying Terraform cloud platform project.", "Body"), Spacer(1, 8), p("Activity-1 Rubrics for MOOC Course Evaluation (Total: 15 Marks)", "HeadingDark")]
rubric = [["Sl.No", "CRITERIA", "MARKS", "MARK Obtained"], ["1", "Course Completion on time", "5", ""], ["2", "Project Presentation", "5", ""], ["3", "Report Writing", "5", ""], ["4", "Total", "15", ""]]
story += [grid(rubric, [0.55*inch, 3.65*inch, 0.8*inch, 1.1*inch]), Spacer(1, 28), p("Date of Submission: 27-09-26", "BodySmall"), Spacer(1, 18), p("Signature of the Student                                      Signature of the Faculty", "BodySmall"), PageBreak()]
story += title_block("INDEX")
index = [["Sl. No.", "Title", "Page No."], ["1", "Course Summary with Screenshot", "4"], ["2", "Course Learning Outcomes", "5"], ["3", "Course Completion Certificate", "6"], ["4", "Project Summary - Problem statement, Architecture, Steps of Implementation, Output", "7-10"], ["5", "Proof Link: GitHub", "11"], ["6", "Conclusion", "12"], ["7", "References", "13"]]
story += [grid(index, [0.75*inch, 5.5*inch, 0.75*inch]), Spacer(1, 22), p("Student: Devyansh Gupta | USN: 25MCAR0193", "CenterSmall"), PageBreak()]
story += title_block("1. COURSE SUMMARY WITH SCREENSHOT", "HashiCorp Certified: Terraform Associate (003) Cert Prep by KodeKloud")
story += [p("This LinkedIn Learning course is an intermediate preparation course for the HashiCorp Certified: Terraform Associate (003) examination. It develops practical skills in infrastructure as code, Terraform CLI usage, providers, resources, variables, state, modules, import, workspaces, logging, and Terraform Cloud.", "Body"), p("Course duration: 3 hours 10 minutes | Level: Intermediate | Completed by: Devyansh Gupta | Completion date: 20 September 2026", "BodySmall")]
if SCREENSHOT.exists():
    story += [Image(str(SCREENSHOT), width=6.9*inch, height=4.63*inch), Spacer(1, 4), p("Figure 1: Course content view showing Terraform modules and Terraform Cloud topics.", "CenterSmall")]
story.append(PageBreak())
story += title_block("2. COURSE LEARNING OUTCOMES")
for h, b in [("Infrastructure as Code", "Understand why infrastructure can be represented as version-controlled, repeatable configuration."), ("Terraform workflow", "Use init, fmt, validate, plan, apply, show, output, and destroy as part of a controlled workflow."), ("State management", "Explain Terraform state, state locking, remote backends, drift, and the role of Terraform Cloud."), ("Reusable configuration", "Use variables, outputs, modules, expressions, and provider configuration to build maintainable projects."), ("Operational confidence", "Read a plan, identify resource dependencies, import existing resources, and troubleshoot with logging.")]:
    story += [p(h, "HeadingDark"), p(b, "Body")]
story += [p("The final project applies these outcomes by defining a secure, repeatable AWS static website platform with S3 and CloudFront resources, outputs, provider constraints, and automated validation.", "Body"), PageBreak()]
story += title_block("3. COURSE COMPLETION CERTIFICATE")
story += [p("Course: LinkedIn Learning - HashiCorp Certified: Terraform Associate (003) Cert Prep by KodeKloud", "Body"), p("Learner: Devyansh Gupta", "Body"), p("Completed: Sep 20, 2026 at 06:50 PM UTC", "Body"), p("Duration: 3 hours 10 minutes", "Body"), p("Top skills covered: DevOps, Terraform", "Body"), p("Certificate ID: 98f20bbe44e7daad5af0259b59fc24ebc3e37489225625644fb6854138dd6646", "BodySmall"), p("The source certificate PDF supplied with this report is the evidence for course completion and is retained separately from this project report.", "Body"), PageBreak()]
story += title_block("4. PROJECT SUMMARY - PROBLEM STATEMENT")
story += [p("Problem statement", "HeadingDark"), p("Manual creation of a website hosting platform is repetitive, difficult to audit, and prone to configuration drift. The project solves this by defining the infrastructure as Terraform code that can be reviewed, validated, versioned, and reproduced.", "Body"), p("Project objective", "HeadingDark"), p("Provision a secure static website platform on AWS using a private S3 bucket as the origin and an Amazon CloudFront distribution as the HTTPS delivery layer. The design prevents direct public access to the bucket and grants read access only to CloudFront through Origin Access Control.", "Body"), p("Scope", "HeadingDark"), p("The repository contains provider and version constraints, variables, outputs, S3 resources, CloudFront resources, an IAM bucket policy, a sample website, GitHub Actions validation, documentation, and a reproducible local validation record.", "Body"), PageBreak()]
story += title_block("4.1 PROJECT ARCHITECTURE")
arch = [["Layer", "Component", "Purpose"], ["Source", "GitHub repository", "Version control, collaboration, and proof link"], ["IaC", "Terraform", "Declarative resource definitions and dependency graph"], ["Storage", "Amazon S3", "Private bucket for website assets"], ["Delivery", "Amazon CloudFront", "HTTPS distribution and caching"], ["Security", "Origin Access Control + bucket policy", "Only CloudFront can read the S3 origin"], ["Automation", "GitHub Actions", "Format, initialize, and validate on pull requests and pushes"]]
story += [grid(arch, [1.0*inch, 1.8*inch, 4.2*inch]), Spacer(1, 20), p("Flow: Developer -> GitHub -> Terraform plan -> AWS S3 + CloudFront -> HTTPS website", "CenterSmall"), PageBreak()]
story += title_block("4.2 STEPS OF IMPLEMENTATION")
steps = ["1. Create Terraform version and AWS provider constraints.", "2. Define configurable region, project name, environment, and CloudFront price class variables.", "3. Create an S3 bucket with public access blocked and versioning enabled.", "4. Create a CloudFront Origin Access Control and distribution with HTTPS redirection.", "5. Create an IAM policy document and attach it to the S3 bucket so CloudFront can read objects.", "6. Expose bucket, distribution ID, and CloudFront domain through Terraform outputs.", "7. Add a sample website and GitHub Actions workflow for formatting and validation.", "8. Run terraform fmt -recursive, terraform init -backend=false, and terraform validate.", "9. Commit and upload the project to GitHub for repeatable review and submission proof."]
for s in steps:
    story += [p(s, "Body")]
story += [p("Validation result: Terraform v1.15.9 reported that the configuration is valid. Applying infrastructure was intentionally not performed because it requires AWS credentials and creates billable cloud resources.", "Body"), PageBreak()]
story += title_block("4.3 OUTPUT")
story += [p("Expected Terraform outputs after a successful AWS apply:", "Body"), p("website_bucket_name - The private S3 bucket containing website assets.", "Body"), p("cloudfront_distribution_id - The CloudFront distribution identifier.", "Body"), p("cloudfront_domain_name - The HTTPS domain name used to access the website.", "Body"), p("Local evidence", "HeadingDark"), p("The repository includes the site/index.html landing page and the GitHub Actions validation workflow. The Terraform configuration has been formatted and validated successfully. The deployment remains ready for an AWS-authenticated plan/apply workflow.", "Body"), p("Security outcome", "HeadingDark"), p("The S3 bucket blocks public access. CloudFront uses Origin Access Control with SigV4 signing, and the bucket policy limits object reads to the CloudFront service principal and distribution ARN.", "Body"), PageBreak()]
story += title_block("5. PROOF LINK: GITHUB")
story += [p("Repository: <link href='https://github.com/Devyansh-Gupta/terraform-cloud-platform-devyansh-25mcar0193'>https://github.com/Devyansh-Gupta/terraform-cloud-platform-devyansh-25mcar0193</link>", "Body"), p("Repository visibility: Private", "Body"), p("Commit: Create Terraform cloud platform project", "Body"), p("The repository contains the complete Terraform source, sample website, workflow, README, provider lock file, and report-generation source. The private setting protects the student identifier while allowing the owner to share access with the evaluator.", "Body"), p("Suggested evaluator commands", "HeadingDark"), p("terraform init<br/>terraform fmt -check -recursive<br/>terraform validate<br/>terraform plan -var=\"project_name=devyansh-terraform-demo\" -var=\"environment=dev\"", "BodySmall"), PageBreak()]
story += title_block("6. CONCLUSION")
story += [p("The LinkedIn Learning course provided the concepts required to design and operate Terraform configurations. The project applies those concepts in an end-to-end cloud platform: infrastructure is declared in code, secured through least-privilege access, exposed through outputs, checked automatically, and published in Git for review.", "Body"), p("The implementation is ready for a credentialed AWS plan and apply. Keeping the apply step behind an explicit approval protects the account from unexpected cost or resource creation while preserving a complete, reproducible submission.", "Body"), Spacer(1, 18), p("Submitted by: Devyansh Gupta<br/>USN: 25MCAR0193<br/>Date of Submission: 27-09-26", "BodySmall"), PageBreak()]
story += title_block("7. REFERENCES")
story += [p("1. LinkedIn Learning. HashiCorp Certified: Terraform Associate (003) Cert Prep by KodeKloud. https://www.linkedin.com/learning/hashicorp-certified-terraform-associate-003-cert-prep-by-kodekloud/", "Body"), p("2. HashiCorp Terraform documentation. https://developer.hashicorp.com/terraform/docs", "Body"), p("3. HashiCorp AWS provider documentation. https://registry.terraform.io/providers/hashicorp/aws/latest/docs", "Body"), p("4. Supplied course completion certificate: CertificateOfCompletion_HashiCorp Certified Terraform Associate 003 Cert Prep by KodeKloud.pdf", "Body"), p("5. Supplied reference report: PCP_25MCAR0144_DHRUVI.pdf", "Body")]
doc = SimpleDocTemplate(str(PDF), pagesize=letter, rightMargin=0.65*inch, leftMargin=0.65*inch, topMargin=0.55*inch, bottomMargin=0.72*inch, title="Devyansh Gupta Terraform Course Project Report", author="Devyansh Gupta")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(PDF)

