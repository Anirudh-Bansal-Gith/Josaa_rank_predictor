import streamlit as st
import pandas as pd
categories = [    'OPEN',
    'EWS',
    'OBC-NCL',
    'SC',
    'ST',
    'OPEN (PwD)',
    'EWS (PwD)',
    'OBC-NCL (PwD)',
    'SC (PwD)',
    'ST (PwD)' ]


states = ['Andaman and Nicobar Islands',
 'Andhra Pradesh',
 'Arunachal Pradesh',
 'Assam',
 'Bihar',
 'Chandigarh',
 'Chhattisgarh',
 'Dadra & Nagar Haveli and Daman & Diu',
 'Delhi',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Ladakh',
 'Lakshadweep',
 'Madhya Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Puducherry',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar Pradesh',
 'Uttarakhand',
 'West Bengal']
branches =  ['All', 'Aeronautical Engineering (4 Years, Bachelor of Technology)',
 'Aerospace Engineering (4 Years, Bachelor of Technology)',
 'Agricultural Engineering (4 Years, Bachelor of Technology)',
 'Animation and VFX (4 Years, Bachelor of Technology)',
 'Architecture (5 Years, Bachelor of Architecture)',
 'Artificial Intelligence (4 Years, Bachelor of Technology)',
 'Artificial Intelligence (5 Years, Integrated B. Tech. and M. Tech.)',
 'Artificial Intelligence and Data Engineering (4 Years, Bachelor of Technology)',
 'Artificial Intelligence and Data Science (4 Years, Bachelor of Technology)',
 'Artificial Intelligence and Machine Learning (4 Years, Bachelor of Technology)',
 'B. Tech in Electronics and Communication Engineering with minor in Wearable Electronics (4 Years, Bachelor of Technology)',
 'B. Tech. and M. Tech. in Engineering and Computational Mechanics (Dual Degree) (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'B.Tech in Artificial Intelligenece and Data Science (Transportation and Logistics) (4 Years, Bachelor of Technology)',
 'B.Tech in Aviation Engineering (4 Years, Bachelor of Technology)',
 'B.Tech in CSE (AI and ML) (4 Years, Bachelor of Technology)',
 'B.Tech in Civil Engineering (Rail Engineering) (4 Years, Bachelor of Technology)',
 'B.Tech in Electrical Engineering ( Rail Engineering) (4 Years, Bachelor of Technology)',
 'B.Tech in Electronics & Communication Engineering (Rail Engineering) (4 Years, Bachelor of Technology)',
 'B.Tech in Mathematics and Computing (4 Years, Bachelor of Technology)',
 'B.Tech in Mechanical Engineering ( Rail Engineering) (4 Years, Bachelor of Technology)',
 'B.Tech in Mechanical Engineering and M.Tech in AI and Robotics (5 Years, B.Tech. + M.Tech./MS (Dual Degree))',
 'B.Tech. (Civil Engineering) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. (Computer Science and Engineering) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. (Elctrical Engineering) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. (Electronics and Communication Engineering) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. (Food Engineering and Technology) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. (Mechanical Engineering) - MBA (5 Years, Bachelor of Technology and MBA (Dual Degree))',
 'B.Tech. in Electronics and Communication Engineering and M.Tech. in Communication Systems (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'B.Tech. in Electronics and Communication Engineering and M.Tech. in Microelectronics and VLSI Systems (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Bachelor of Design (4 Years, Bachelor of Design)',
 'Bio Medical Engineering (4 Years, Bachelor of Technology)',
 'Bio Technology (4 Years, Bachelor of Technology)',
 'Biomedical Engineering (4 Years, Bachelor of Technology)',
 'Biosciences and Bioengineering (4 Years, Bachelor of Technology)',
 'Biotechnology (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Biotechnology and Biochemical Engineering (4 Years, Bachelor of Technology)',
 'CSE ( Data Science & Analytics) (4 Years, Bachelor of Technology)',
 'Carpet and Textile Technology (4 Years, Bachelor of Technology)',
 'Ceramic Engineering (4 Years, Bachelor of Technology)',
 'Ceramic Engineering and M.Tech Industrial Ceramic (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Chemical Engineering (4 Years, Bachelor of Technology)',
 'Chemical Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Chemical Engineering (5 Years, Integrated Masters in Technology)',
 'Chemical Science and Technology (4 Years, Bachelor of Technology)',
 'Chemical Technology (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Chemistry (5 Years, Bachelor of Science and Master of Science (Dual Degree))',
 'Chemistry (5 Years, Integrated Master of Science)',
 'Civil Engineering (4 Years, Bachelor of Technology)',
 'Civil Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Civil Engineering with Specialization in Construction Technology and Management (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Civil and Environmental Engineering (4 Years, Bachelor of Technology)',
 'Computational Mathematics (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Computational and Data Science (4 Years, Bachelor of Technology)',
 'Computer Engineering (4 Years, Bachelor of Technology)',
 'Computer Science (4 Years, Bachelor of Technology)',
 'Computer Science Engineering (Artificial Intelligence) (4 Years, B. Tech / B. Tech (Hons.))',
 'Computer Science Engineering (Artificial lntelligence and Machine Learning) (4 Years, Bachelor of Technology)',
 'Computer Science Engineering (Data Science and Analytics) (4 Years, Bachelor of Technology)',
 'Computer Science Engineering (Data Science) (4 Years, B. Tech / B. Tech (Hons.))',
 'Computer Science Engineering (Human Computer lnteraction and Gaming Technology) (4 Years, Bachelor of Technology)',
 'Computer Science and Artificial Intelligence (4 Years, Bachelor of Technology)',
 'Computer Science and Business (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering ( Artificial Intelligence & Data Science) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Computer Science and Engineering (Artificial Intelligence and Machine Learning) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (Artificial Intelligence) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (Cyber Physical System) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (Cyber Security) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (Data Science) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (Internet of Things, Cyber Security including Block Chain Technology ) (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering (with Specialization of Data Science and Artificial Intelligence) (4 Years, B. Tech / B. Tech (Hons.))',
 'Computer Science and Engineering with Major in Artificial Intelligence (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering with Specialization in Cyber Security (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Computer Science and Engineering with Specialization in Data Science (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Computer Science and Engineering with minor in AI and ML (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering with specialization in Artificial Intelligence and Data Science (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering with specialization in Cyber Security (4 Years, Bachelor of Technology)',
 'Computer Science and Engineering with specialization in Quantum Technologies (4 Years, Bachelor of Technology)',
 'Dairy Engineering (4 Years, Bachelor of Technology)',
 'Data Science and Artificial Intelligence (4 Years, Bachelor of Technology)',
 'Data Science and Engineering (4 Years, Bachelor of Technology)',
 'Design Engineering (4 Years, Bachelor of Technology)',
 'Electrical Engineering (4 Years, Bachelor of Technology)',
 'Electrical Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Electrical Engineering with Specialization In Power System Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Electrical and Electronics Engineering (4 Years, Bachelor of Technology)',
 'Electronic Engineering (4 Years, Bachelor of Technology)',
 'Electronics Engineering (VLSI Design and Technology) (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Electronics and Communication Engineering (Avionics) (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (Internet of Things) (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (VLSI Design and Technology) (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (VLSI Design) (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering (with Specialization of Embedded Systems and Internet of Things) (4 Years, B. Tech / B. Tech (Hons.))',
 'Electronics and Communication Engineering with Specialization in Microelectronics and VLSI System Design (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Electronics and Communication Engineering with specialization in Design and Manufacturing (4 Years, Bachelor of Technology)',
 'Electronics and Communication Engineering with specialization in VLSI and Embedded Systems (4 Years, Bachelor of Technology)',
 'Electronics and Instrumentation Engineering (4 Years, Bachelor of Technology)',
 'Electronics and Telecommunication Engineering (4 Years, Bachelor of Technology)',
 'Electronics and VLSI Engineering (4 Years, Bachelor of Technology)',
 'Energy Engineering (4 Years, Bachelor of Technology)',
 'Energy and Electrical Vehicle Engineering (4 Years, Bachelor of Technology)',
 'Engineering Physics (4 Years, Bachelor of Technology)',
 'Engineering Physics (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Engineering and Computational Mechanics (4 Years, Bachelor of Technology)',
 'Fashion and Apparel Engineering (4 Years, Bachelor of Technology)',
 'Food Engineering and Technology (4 Years, Bachelor of Technology)',
 'Food Process Engineering (4 Years, Bachelor of Technology)',
 'Food Technology (4 Years, Bachelor of Technology)',
 'Food Technology and Management (4 Years, Bachelor of Technology)',
 'Handloom and Textile Technology (4 Years, Bachelor of Technology)',
 'Industrial Chemistry (4 Years, Bachelor of Technology)',
 'Industrial Design (4 Years, Bachelor of Technology)',
 'Industrial Internet of Things (4 Years, Bachelor of Technology)',
 'Industrial and Production Engineering (4 Years, Bachelor of Technology)',
 'Information Technology (4 Years, Bachelor of Technology)',
 'Information Technology-Business Informatics (4 Years, Bachelor of Technology)',
 'Instrumentation Engineering (4 Years, Bachelor of Technology)',
 'Instrumentation and Control Engineering (4 Years, Bachelor of Technology)',
 'Integrated B. Tech.(IT) and M. Tech (IT) (5 Years, Integrated B. Tech. and M. Tech.)',
 'Integrated B. Tech.(IT) and MBA (5 Years, Integrated B. Tech. and MBA)',
 'Life Science (5 Years, Integrated Master of Science)',
 'Material Science and Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Materials Engineering (4 Years, Bachelor of Technology)',
 'Materials Engineering (5 Years, Integrated Master of Technology)',
 'Materials Science and Engineering (4 Years, Bachelor of Technology)',
 'Materials Science and Metallurgical Engineering (4 Years, Bachelor of Technology)',
 'Mathematics & Computing (5 Years, Bachelor of Science and Master of Science (Dual Degree))',
 'Mathematics (5 Years, Integrated Master of Science)',
 'Mathematics and Computing (4 Years, Bachelor of Technology)',
 'Mathematics and Computing (5 Years, Integrated Master of Science)',
 'Mathematics and Computing Technology (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Mathematics and Data Science (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Mathematics and Scientific Computing (4 Years, Bachelor of Technology)',
 'Mechanical Engineering (4 Years, Bachelor of Technology)',
 'Mechanical Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Mechanical Engineering with Specialization in Manufacturing and Industrial Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Mechanical Engineering with specialization in Design and Manufacturing (4 Years, Bachelor of Technology)',
 'Mechatronics Engineering (4 Years, Bachelor of Technology)',
 'Mechatronics and Automation Engineering (4 Years, Bachelor of Technology)',
 'Metallurgical and Materials Engineering (4 Years, Bachelor of Technology)',
 'Metallurgical and Materials Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Metallurgy and Materials Engineering (4 Years, Bachelor of Technology)',
 'Microelectronics & VLSI Engineering (4 Years, Bachelor of Technology)',
 'Mining Engineering (4 Years, Bachelor of Technology)',
 'Mining Engineering (5 Years, Bachelor and Master of Technology (Dual Degree))',
 'Physics (5 Years, Bachelor of Science and Master of Science (Dual Degree))',
 'Physics (5 Years, Integrated Master of Science)',
 'Physics and Computational Engineering (4 Years, Bachelor of Technology)',
 'Planning (4 Years, Bachelor of Planning)',
 'Printing and Packaging Technology (4 Years, Bachelor of Technology)',
 'Production Engineering (4 Years, Bachelor of Technology)',
 'Production and Industrial Engineering (4 Years, Bachelor of Technology)',
 'Quantitative Economics & Data Science (5 Years, Integrated Master of Science)',
 'ROBOTICS & AUTOMATION (4 Years, Bachelor of Technology)',
 'Robotics and AI (4 Years, Bachelor of Technology)',
 'SUSTAINABLE ENERGY TECHNOLOGIES (4 Years, Bachelor of Technology)',
 'Smart Manufacturing (4 Years, Bachelor of Technology)',
 'Textile Technology (4 Years, Bachelor of Technology)',
 'VLSI Design and Technology (4 Years, Bachelor of Technology)']


brand_mapped_institutes = {'NIT':['Dr. B R Ambedkar National Institute of Technology, Jalandhar',
 'Malaviya National Institute of Technology Jaipur',
 'Maulana Azad National Institute of Technology Bhopal',
 'Motilal Nehru National Institute of Technology Allahabad',
 'National Institute of Technology Agartala',
 'National Institute of Technology, Andhra Pradesh',
 'National Institute of Technology Arunachal Pradesh',
 'National Institute of Technology Calicut',
 'National Institute of Technology Delhi',
 'National Institute of Technology Durgapur',
 'National Institute of Technology Goa',
 'National Institute of Technology Hamirpur',
 'National Institute of Technology, Jamshedpur',
 'National Institute of Technology Karnataka, Surathkal',
 'National Institute of Technology, Kurukshetra',
 'National Institute of Technology, Manipur',
 'National Institute of Technology Meghalaya',
 'National Institute of Technology, Mizoram',
 'National Institute of Technology Nagaland',
 'National Institute of Technology Patna',
 'National Institute of Technology Puducherry',
 'National Institute of Technology Raipur',
 'National Institute of Technology, Rourkela',
 'National Institute of Technology Sikkim',
 'National Institute of Technology, Silchar',
 'National Institute of Technology, Srinagar',
 'National Institute of Technology, Tiruchirappalli',
 'National Institute of Technology, Uttarakhand',
 'National Institute of Technology, Warangal',
 'Sardar Vallabhbhai National Institute of Technology, Surat',
 'Visvesvaraya National Institute of Technology, Nagpur',
 'Indian Institute of Engineering Science and Technology, Shibpur'], 
 'IIIT':['Atal Bihari Vajpayee Indian Institute of Information Technology & Management Gwalior',
 'Indian Institute of Information Technology (IIIT)Kota, Rajasthan',
 'Indian Institute of Information Technology(IIIT) Una, Himachal Pradesh',
 'Indian Institute of Information Technology (IIIT), Sri City, Chittoor',
 'Indian Institute of Information Technology(IIIT), Vadodara, Gujrat',
 'Indian Institute of Information Technology Allahabad',
 'Indian Institute of Information Technology Bhagalpur',
 'Indian Institute of Information Technology Bhopal',
 'Indian Institute of Information Technology Design & Manufacturing Kurnool, Andhra Pradesh',
 'Indian Institute of Information Technology(IIIT) Dharwad',
 'Indian Institute of Information Technology Guwahati',
 'Indian Institute of Information Technology(IIIT) Kalyani, West Bengal',
 'Indian Institute of Information Technology(IIIT) Kottayam',
 'Indian Institute of Information Technology Lucknow',
 'INDIAN INSTITUTE OF INFORMATION TECHNOLOGY SENAPATI MANIPUR',
 'Indian Institute of Information Technology (IIIT) Nagpur',
 'Indian Institute of Information Technology (IIIT) Pune',
 'Indian institute of information technology, Raichur, Karnataka',
 'Indian Institute of Information Technology (IIIT) Ranchi',
 'Indian Institute of Information Technology(IIIT) Kilohrad, Sonepat, Haryana',
 'Indian Institute of Information Technology Surat',
 'Indian Institute of Information Technology Tiruchirappalli',
 'Indian Institute of Information Technology, Vadodara International Campus Diu (IIITVICD)',
 'Indian Institute of Information Technology, Agartala',
 'Indian Institute of Information Technology, Design & Manufacturing, Kancheepuram',
 'Pt. Dwarka Prasad Mishra Indian Institute of Information Technology, Design & Manufacture Jabalpur'], 
 'GFTI':['Assam University, Silchar',
 'Birla Institute of Technology, Deoghar Off-Campus',
 'Birla Institute of Technology, Mesra, Ranchi',
 'Birla Institute of Technology, Patna Off-Campus',
 'CU Jharkhand',
 'Central University of Haryana',
 'Central University of Jammu',
 'Central University of Rajasthan, Rajasthan',
 'Central institute of Technology Kokrajar, Assam',
 'Chhattisgarh Swami Vivekanada Technical University, Bhilai (CSVTU Bhilai)',
 'Gati Shakti Vishwavidyalaya, Vadodara',
 'Ghani Khan Choudhary Institute of Engineering and Technology, Malda, West Bengal',
 'Gurukula Kangri Vishwavidyalaya, Haridwar',
 'Indian Institute of Carpet Technology, Bhadohi',
 'Indian Institute of Handloom Technology(IIHT), Varanasi',
 'Indian Institute of Handloom Technology, Salem',
 'Institute of Chemical Technology, Mumbai: Indian Oil Odisha Campus, Bhubaneswar',
 'Institute of Engineering and Technology, Dr. H. S. Gour University. Sagar (A Central University)',
 'Institute of Infrastructure, Technology, Research and Management-Ahmedabad',
 'International Institute of Information Technology, Bhubaneswar',
 'International Institute of Information Technology, Naya Raipur',
 'Islamic University of Science and Technology Kashmir',
 'J.K. Institute of Applied Physics & Technology, Department of Electronics & Communication, University of Allahabad- Allahabad',
 'Jawaharlal Nehru University, Delhi',
 'Mizoram University, Aizawl',
 'National Institute of Advanced Manufacturing Technology, Ranchi',
 'National Institute of Electronics and Information Technology, Ajmer (Rajasthan)',
 'National Institute of Electronics and Information Technology, Aurangabad (Maharashtra)',
 'National Institute of Electronics and Information Technology, Gorakhpur (UP)',
 'National Institute of Electronics and Information Technology, Patna (Bihar)',
 'National Institute of Electronics and Information Technology, Ropar (Punjab)',
 'National Institute of Food Technology Entrepreneurship and Management, Kundli',
 'National Institute of Food Technology Entrepreneurship and Management, Thanjavur',
 'North Eastern Regional Institute of Science and Technology, Nirjuli-791109 (Itanagar),Arunachal Pradesh',
 'North-Eastern Hill University, Shillong',
 'Puducherry Technological University, Puducherry',
 'Punjab Engineering College, Chandigarh',
 'Rajiv Gandhi National Aviation University, Fursatganj, Amethi (UP)',
 'Sant Longowal Institute of Engineering and Technology',
 'School of Engineering, Tezpur University, Napaam, Tezpur',
 'School of Planning & Architecture, Bhopal',
 'School of Planning & Architecture, New Delhi',
 'School of Planning & Architecture: Vijayawada',
 'School of Studies of Engineering and Technology, Guru Ghasidas Vishwavidyalaya, Bilaspur',
 'Shri G. S. Institute of Technology and Science Indore',
 'Shri Mata Vaishno Devi University, Katra, Jammu & Kashmir',
 'University of Hyderabad'] }




st.set_page_config(    page_title="JoSAA College Predictor",
    page_icon="🎓",
    layout="wide")

st.title('Predictor')
st.header('JOSAA College Predictor')

with st.container(border=True):
    st.subheader("📍 Your Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        quota = st.selectbox('Please select your eligible Quota', categories, index= None)
        rank = st.number_input('Category Rank', min_value=0, value = None)
        state = st.selectbox('Please select your home state/UT', states , index = None)

    with col2:
        gender = st.selectbox('Gender', ['Gender-Neutral', 'Female-only (including Supernumerary)'], index=None)
        branch = st.multiselect('Branch',branches, default=[])

    with col3:
        brands = st.multiselect('Select Brand', ['NIT', 'IIIT', 'GFTI'])
        if brands:
            institutes_avialable = []
            for choice in brands:
                institutes_avialable.extend(list(brand_mapped_institutes[choice]))
            institutes_wished = st.multiselect('Institute', institutes_avialable, default = [])
        st.write("") # Spacing
        predict_btn = st.button("🚀 Predict My Colleges", use_container_width=True, type="primary")



st.divider()

if quota and state and gender and rank and predict_btn and branch and brands: 
    data = pd.read_csv('JOSAA_OR_CR_DATA_JEE_MAINS.csv')
    del data['Unnamed: 0']

    # --- Mandatory Constraints ---
    conditions = (
        (data['Seat Type'] == quota) & 
        (data['Gender'] == gender) & 
        (data['Closing Rank'] >= rank)
    )

    # IIIT
    condition_iiit = (data['Brand'] == 'IIIT')

    # GFTI
    condition_gfti_home = (
        (data['Brand'] == 'GFTI') & 
        (data['State'] == state) & 
        (data['Quota'] == 'HS')
    )

    condition_gfti_away = (
        (data['Brand'] == 'GFTI') & 
        (data['Quota'].isin(['AI','OS'])) 
    )

    condition_gfti = condition_gfti_home | condition_gfti_away

    # NIT
    eligible_home_states = [state]

    if state == 'Chandigarh':
        eligible_home_states.append('Delhi')
    elif state == 'Ladakh':
        eligible_home_states.append('Jammu & Kashmir')
    elif state in ['Daman & Diu', 'Dadra & Nagar Haveli']:
        eligible_home_states.append('Gujarat')
    elif state == 'Lakshadweep':
        eligible_home_states.append('Kerala')
    elif state == 'Andaman & Nicobar Islands':
        eligible_home_states.append('West Bengal')

    condition_nit_home = (
        (data['Brand'] == 'NIT') &
        (data['State'].isin(eligible_home_states)) &
        (data['Quota'].isin(['HS', 'LA', 'JK', 'GO']))
    )

    condition_nit_away = (
        (data['Brand'] == 'NIT') &
        (~data['State'].isin(eligible_home_states)) & 
        (data['Quota'] == 'OS')
    )

    condition_nit = condition_nit_away | condition_nit_home

    # --- Final Combined Boolean ---
    net = conditions & (condition_nit | condition_gfti | condition_iiit)
    data[net].sort_values(by=[ 'Closing Rank', 'Opening Rank'])
    output = data[net].sort_values(by=[ 'Closing Rank', 'Opening Rank'])
    output = output[output['Brand'].isin(brands)]
    if 'All' not in branch:
            output= output[output['Academic Program Name'].isin(branch)]
    if institutes_wished:
        output = output[output['Institute'].isin(institutes_wished)]

    st.dataframe(
        output,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Opening Rank": st.column_config.NumberColumn(format="%d"),
            "Closing Rank": st.column_config.NumberColumn(format="%d"),
        }
    )
