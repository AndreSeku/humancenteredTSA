import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Low-Code Data Science',
    Svg: require('../../static/img/iconmonstr-code-thin.svg').default,
    description: (
      <>
        Build your own Data Science Pipeline just with a few lines of code. Run the Pipeline and receive your analysis results visualized or descriptive.
      </>
    ),
  },
  {
    title: 'No-Code Data Science',
    Svg: require('../../static/img/iconmonstr-product-6.svg').default,
    description: (
      <>
        The hcTSA-package comes with a Webserver. Hence, it is possible to use it as a backend for No-Code applications.
      </>
    ),
  },
  {
    title: 'Human-Centered Data Science',
    Svg: require('../../static/img/iconmonstr-circle-thin.svg').default,
    description: (
      <>
        With the hcTSA-package, you can focus on the real user's problem and develop a human-centered data science application.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
